# Appunti esperimenti preliminari — generazione di unit test con LLM

*Note di lavoro, agosto 2026. Testo da riadattare per le sezioni della tesi su Overleaf.*

## Contesto e obiettivo

Il punto di partenza è il paper "TestGenEval" (https://openreview.net/pdf?id=7o6SG5gVev), in cui gli LLM generano unit test senza particolari informazioni di contesto. L'ipotesi della tesi è che la coverage migliori dando al modello: (1) contesto strutturale sul codice, (2) strumenti software di supporto, (3) feedback iterativo dall'esecuzione dei test e dal report di coverage.

La pipeline prevista ha tre fasi:

1. **Contesto**: passare al modello il file sorgente oppure una rappresentazione di più alto livello (AST), ed eventualmente uno scheletro di test generato automaticamente (Klara).
2. **Generazione iterativa**: per ogni test generato, eseguirlo e restituire al modello eventuali errori, iterando fino a test funzionanti.
3. **Feedback di coverage**: calcolare la coverage e passare al modello le righe non coperte, chiedendo test mirati per quelle righe.

## Esperimento 1 — libreria `ast` (standard library)

File: `esperimenti/01_ast/prova_ast.py`, applicato a `esperimenti/funzioni_esempio.py` (tre funzioni di difficoltà crescente: senza rami, con if/elif, con ciclo ed eccezione).

Con `ast.parse` si ottiene l'albero sintattico; visitandolo con `ast.walk` si estraggono per ogni funzione: nome e argomenti, docstring, numero di `return` e di `if`, eccezioni sollevate, righe di inizio/fine.

Osservazioni utili per la tesi:

- Il riassunto strutturale è molto più compatto del file sorgente: utile come contesto per l'LLM quando il file è grande (limiti di finestra di contesto, costo per token).
- Il numero di `if` è correlato al numero di cammini di esecuzione, quindi suggerisce *quanti* test servono per la branch coverage.
- Le eccezioni estratte (`ValueError` in `media_positivi`) indicano che serve un test con `pytest.raises`.
- `lineno`/`end_lineno` permettono di mappare le righe non coperte (dal report di coverage) alla funzione corrispondente: sarà il collegamento tra fase 3 e fase 1 della pipeline.

## Esperimento 2 — Klara

File: `esperimenti/02_klara/`. Installazione: `pip install klara` (versione 0.6.3, 2021).

**Limite riscontrato**: Klara va in crash sul file di esempio completo (non supporta list comprehension, eccezioni, e in generale Python moderno). Sul sottoinsieme supportato (aritmetica su interi, if/elif) funziona bene: comando `klara funzioni_per_klara.py` → genera `test_funzioni_per_klara.py`.

Risultato notevole: Klara usa il solver SMT Z3 per trovare input che coprono ogni ramo. Per `classifica_voto` ha trovato da sola i valori di confine 0, 18, 24, 28 — esattamente i boundary value che un tester umano sceglierebbe. I test generati sono però "scheletri": gli assert contengono i valori attesi dedotti simbolicamente, corretti ma senza semantica (nomi generici `test_funzione_0`).

Ruolo previsto nella pipeline: generare lo scheletro iniziale da cui l'LLM parte (fase 1), lasciando all'LLM i casi che Klara non copre (eccezioni, strutture dati, codice moderno).

## Esperimento 3 — ciclo test + coverage

I test generati da Klara passano tutti (`pytest`: 3 passed) e raggiungono il 100% di statement coverage (`coverage report -m` con la colonna `Missing` vuota). La colonna `Missing` del report è esattamente l'informazione da restituire all'LLM nella fase 3: elenca le righe non coperte.

## Esperimento 4 — simulazione manuale del loop con LLM (via chat)

Prima esecuzione dell'intera pipeline con un LLM vero, in versione manuale: l'LLM è stato usato tramite chat, e il copia-incolla umano ha fatto le veci dello script di orchestrazione.

Procedura: chiesti test pytest per la sola `media_positivi` (file `esperimenti/test_llm1.py`) → 11 test, tutti passati al primo colpo → coverage di `funzioni_esempio.py` al **47%** (Missing: riga 12 e righe 17-24, cioè `somma` e `classifica_voto`, mai richieste) → riportate all'LLM le righe mancanti → nuovi test mirati → coverage al **100%** in una sola iterazione di feedback.

Osservazione critica: su funzioni così semplici il 100% è quasi garantito e non dimostra l'ipotesi. L'esperimento valida la *meccanica* del ciclo (genera → esegui → misura → feedback → migliora), non la sua *utilità*, che va misurata su codice dove il primo tentativo fallisce. Da qui la domanda sul benchmark (punto 2).

## Esperimento 5 — loop su funzioni più complesse e scoperta di codice morto

File: `esperimenti/03_ciclo/`. Bersaglio `funzioni_brutte.py`: tre funzioni con rami annidati, eccezioni e casi limite (`calcola_sconto`, `valida_password`, `interpreta_orario`), 49 statement.

Primo giro: l'LLM (via chat, stesso protocollo manuale) genera 46 test, tutti passati, coverage **98%**. Unica riga scoperta: la 33 (`prezzo = 0`, ramo `if prezzo < 0` di `calcola_sconto`).

Analisi della riga 33: è **irraggiungibile**. Il totale è ≥ 0 (il negativo solleva `ValueError` prima), gli sconti moltiplicano per 0.8/0.9 (mai sotto zero) e il coupon sottrae 5 solo quando il prezzo supera 30 (residuo ≥ 25). La condizione `prezzo < 0` è sempre falsa: è codice difensivo morto, e nessun test potrà mai coprirlo.

Due implicazioni per il sistema:

1. **Criterio di stop**: il loop non può fermarsi "al 100%", deve fermarsi quando la coverage smette di migliorare (plateau) o dopo N iterazioni, altrimenti su codice con righe irraggiungibili itererebbe all'infinito.
2. **Valore diagnostico delle righe residue**: le righe che restano scoperte dopo il plateau sono candidate a essere codice morto o difensivo — informazione utile di per sé per il programmatore. Nota: dimostrare formalmente l'irraggiungibilità (insoddisfacibilità del vincolo) è il mestiere dei solver SMT come Z3, lo stesso usato da Klara: possibile punto di contatto tra i due approcci.

## Punti aperti (da discutere il 4 agosto)

1. **Accesso API a un LLM**: per la pipeline serve chiamare un modello da Python. L'università fornisce crediti/chiavi API? Quale modello usare?
2. **Benchmark**: su quali progetti/funzioni valutare? Riusare i benchmark del paper per confrontarsi direttamente?
3. **Metriche**: statement coverage, branch coverage (`coverage run --branch`), o anche mutation score?
4. **Klara**: vale la pena tenerla vista l'incompatibilità con Python moderno, o meglio usare solo AST + feedback? (Alternativa: usarla solo sul sottoinsieme di funzioni che supporta.)
5. **Baseline**: la baseline sarà "LLM senza contesto" come nel paper, per misurare il contributo di ogni componente (ablation)?
6. **Criterio di stop del loop** (dall'esperimento 5): fermarsi al plateau di coverage o a N iterazioni? E come trattare le righe che restano scoperte — segnalarle come possibile codice morto?
