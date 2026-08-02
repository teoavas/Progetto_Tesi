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

## Punti aperti (da discutere il 4 agosto)

1. **Accesso API a un LLM**: per la pipeline serve chiamare un modello da Python. L'università fornisce crediti/chiavi API? Quale modello usare?
2. **Benchmark**: su quali progetti/funzioni valutare? Riusare i benchmark del paper per confrontarsi direttamente?
3. **Metriche**: statement coverage, branch coverage (`coverage run --branch`), o anche mutation score?
4. **Klara**: vale la pena tenerla vista l'incompatibilità con Python moderno, o meglio usare solo AST + feedback? (Alternativa: usarla solo sul sottoinsieme di funzioni che supporta.)
5. **Baseline**: la baseline sarà "LLM senza contesto" come nel paper, per misurare il contributo di ogni componente (ablation)?
