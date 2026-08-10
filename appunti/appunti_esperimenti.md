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

## Nuova direzione dopo l'incontro del 4 agosto

Il progetto assume la forma di uno **studio di misura** sulla generazione di unit test con LLM di piccola taglia. Impianto sperimentale definito con la relatrice:

- **Dataset**: [UnLeakedTestBench](https://github.com/huangd1999/UnLeakedTestBench), file `ULT_Lite.jsonl`. Campi: `func_name`, `code` (funzione autonoma), `prompt` (descrizione in linguaggio naturale), `task_id`, `test_list` (assert di riferimento umani). Si parte da 20 campioni, obiettivo 100.
- **Modelli**: tre Llama di taglia crescente (1B, 3B, 8B) dal catalogo NVIDIA build, in modo da osservare l'effetto della dimensione del modello.
- **Condizioni**: temperatura 0 (output deterministico, una generazione per campione), template di prompt fissato e dichiarato, output salvati in file separati.
- **Metriche**: (i) coverage effettiva del codice sotto test; (ii) quante volte ogni riga viene rieseguita; (iii) quante righe sono duplicate tra i file di test; (iv) classificazione degli esiti in *passato*, *eseguibile ma fallito*, *non eseguibile*.
- **Confronto senza LLM** (secondario): la stessa valutazione applicata ai test prodotti da AST + Klara.

Rispetto all'ipotesi iniziale, il ciclo di feedback iterativo non fa parte di questa fase: qui si misura il comportamento dei modelli "a colpo singolo", che costituisce la base di riferimento rispetto a cui un eventuale sistema iterativo andrebbe confrontato. Gli esperimenti 1-5 di questo documento restano come lavoro pilota.

Note tecniche rilevate in fase di progettazione: `coverage.py` registra solo se una riga è stata eseguita, non quante volte (per il conteggio serve un tracciatore basato su `sys.settrace`/`sys.monitoring`); la distinzione tra codice non eseguibile e test falliti si ottiene combinando un controllo sintattico con `ast.parse` e i codici di uscita di pytest (2 = errore di raccolta, 1 = test falliti, 0 = tutti passati).

## Esperimento 6 — messa a punto della generazione su NVIDIA build

**Setup finale.** Modelli `meta/llama-3.2-1b-instruct`, `meta/llama-3.2-3b-instruct`, `meta/llama-3.1-8b-instruct` serviti da NVIDIA build tramite libreria `openai` (`base_url = https://integrate.api.nvidia.com/v1`). Temperatura 0, `max_tokens` 1024, una funzione per richiesta, prompt fisso a tre sezioni `[instruction]` / `[data]` / `[format]`. Dataset ULT_Lite (200 campioni, se ne usano i primi 100 nell'ordine del file). Ogni generazione viene salvata in un file separato `generati/<modello>/test_<indice>_<funzione>.py`.

**Instabilità del servizio (da riportare come nota metodologica).** Nella prima sessione le richieste di inferenza andavano sistematicamente in timeout, mentre l'elenco dei modelli rispondeva regolarmente. Le prove condotte per isolare la causa hanno escluso: chiave e connessione (l'endpoint dei modelli rispondeva), il codice (lo script della relatrice dava lo stesso esito), la rete (stesso comportamento da rete fissa e da hotspot), la temperatura, `max_tokens`, la lunghezza del prompt e lo streaming. Anche una richiesta banale, identica a una che era riuscita pochi minuti prima, falliva. Il modello da 70B rispondeva invece regolarmente. In una sessione successiva, senza alcuna modifica al codice, tutte le richieste sono passate al primo tentativo con un tempo medio di 5,5 secondi. Conclusione: disponibilità intermittente degli endpoint, non riproducibile e indipendente dal client. Per questo lo script include un meccanismo di tentativi ripetuti.

**Primi risultati sul modello 8B (100 campioni).**

| esito | sintassi valida | sintassi non valida |
|---|---|---|
| risposta completa (`finish_reason = stop`), 90 casi | 90 | 0 |
| risposta troncata (`finish_reason = length`), 10 casi | 2 | 8 |

Osservazioni:

- Quando il modello conclude da sé, il codice prodotto è **sempre** sintatticamente valido (90/90). Tutti i casi di codice non valido derivano dal troncamento.
- Il troncamento è causato dalla violazione del vincolo sul numero di test: il prompt ne chiede da 3 a 8, ma nei casi troncati il modello arriva a scriverne 13, 17, 23, esaurendo il budget di token.
- Due campioni troncati (37 e 77) superano comunque il controllo sintattico, perché il taglio è caduto a fine funzione: sono file incompleti che sembrano sani. Per questo `finish_reason` va trattato come categoria a sé e non ci si può basare solo sull'analisi sintattica.
- Il controllo di validità è fatto con `ast.parse`, che analizza il codice senza eseguirlo: è il primo filtro della classificazione richiesta (non eseguibile → eseguibile ma fallito → passato).

**Aderenza al formato.** In quattro casi il modello ha incapsulato l'output in un blocco markdown nonostante il divieto esplicito nel prompt; la percentuale di rispetto del formato è essa stessa una misura da riportare. Il modello 70B (usato solo come controllo) ha invece rispettato import e formato al primo tentativo, mentre il modello 1B in una prova preliminare in locale aveva sbagliato l'import, ricadendo su `import pytest`.

## Punti aperti (dal lavoro preliminare, prima del 4 agosto)

1. **Accesso API a un LLM**: per la pipeline serve chiamare un modello da Python. L'università fornisce crediti/chiavi API? Quale modello usare?
2. **Benchmark**: su quali progetti/funzioni valutare? Riusare i benchmark del paper per confrontarsi direttamente?
3. **Metriche**: statement coverage, branch coverage (`coverage run --branch`), o anche mutation score?
4. **Klara**: vale la pena tenerla vista l'incompatibilità con Python moderno, o meglio usare solo AST + feedback? (Alternativa: usarla solo sul sottoinsieme di funzioni che supporta.)
5. **Baseline**: la baseline sarà "LLM senza contesto" come nel paper, per misurare il contributo di ogni componente (ablation)?
6. **Criterio di stop del loop** (dall'esperimento 5): fermarsi al plateau di coverage o a N iterazioni? E come trattare le righe che restano scoperte — segnalarle come possibile codice morto?
