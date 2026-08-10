# Appunti di lavoro — generazione di unit test con LLM

*Note tenute durante il lavoro, da riadattare per le sezioni della tesi su Overleaf.*

## 1. Contesto e riferimento

Il riferimento è TestGenEval (ICLR 2025, https://openreview.net/pdf?id=7o6SG5gVev): un benchmark costruito su SWE-bench con 68.647 test da 1.210 coppie file codice-test, tratte da 11 repository Python reali. Valuta due compiti — generazione dell'intera test suite e completamento di una suite esistente — con metriche di esecuzione (pass@1, pass@5), coverage e mutation score, quest'ultimo ottenuto iniettando bug sintetici nel codice e misurando quanti vengono scoperti dai test.

Il risultato principale è che i modelli faticano sui progetti reali: il migliore (GPT-4o) si ferma a una coverage media del 35,2% e a un mutation score del 18,8%. La causa individuata dagli autori è la difficoltà dei modelli a ragionare sull'esecuzione del codice, con frequenti errori nelle assert sui cammini complessi.

## 2. Oggetto di questa tesi

Misurare la qualità degli unit test generati da modelli di piccola taglia (Llama 1B, 3B, 8B) su funzioni Python reali, a parità di prompt e con temperatura 0, secondo quattro dimensioni: copertura del codice, ripetizione delle righe eseguite, duplicazione fra i test prodotti, ed esito dell'esecuzione (passato / eseguibile ma fallito / non eseguibile).

## 3. Impianto sperimentale

**Dataset.** UnLeakedTestBench, file `ULT_Lite.jsonl`: 200 campioni, uno per riga in formato JSON Lines. Ogni campione contiene il nome della funzione, il suo codice sorgente (funzione autonoma, eseguibile in isolamento), una descrizione in linguaggio naturale, un identificativo e una lista di assert scritti da umani. Si usano i primi 100 campioni nell'ordine del file. Le funzioni vanno da 8 a 171 righe, con mediana 34.

**Modelli.** `meta/llama-3.2-1b-instruct`, `meta/llama-3.2-3b-instruct` e `meta/llama-3.1-8b-instruct`, serviti da NVIDIA build attraverso un'interfaccia compatibile con la libreria `openai`. Il modello da 70B è stato usato unicamente come controllo di funzionamento e non fa parte dello studio.

**Prompt.** Template fisso in tre sezioni. `[instruction]` elenca i vincoli: stile pytest senza classi, import esplicito della funzione sotto test, da 3 a 8 funzioni di test con nomi numerati, almeno un assert per test, divieto di riscrivere la funzione, divieto di spiegazioni e markdown. `[data]` contiene il solo codice della funzione (la descrizione in linguaggio naturale non viene passata). `[format]` mostra lo scheletro atteso dell'output: per i modelli piccoli, vedere la forma è più efficace che leggerne la descrizione.

**Parametri.** Temperatura 0, `max_tokens` 1024, una funzione per richiesta, output salvato in un file separato per ogni coppia (modello, campione).

## 4. Risultati preliminari — modello 8B su 100 campioni

| esito della richiesta | sintassi valida | sintassi non valida |
|---|---|---|
| risposta completa (`finish_reason = stop`) — 90 casi | 90 | 0 |
| risposta troncata (`finish_reason = length`) — 10 casi | 2 | 8 |

Osservazioni:

- Quando il modello conclude da sé, il codice prodotto è sempre sintatticamente valido (90 casi su 90). Tutti i casi di codice non valido derivano dal troncamento, non da un errore di sintassi del modello.
- Il troncamento nasce dalla violazione di un vincolo del prompt: si chiedono da 3 a 8 test, ma nei casi troncati il modello arriva a scriverne 13, 17 o 23, esaurendo il budget di token.
- Due campioni troncati superano comunque il controllo sintattico, perché il taglio è caduto a fine funzione: sono file incompleti che appaiono sani. `finish_reason` va quindi trattato come categoria a sé, senza affidarsi al solo controllo sintattico.
- Il controllo di validità usa `ast.parse`, che analizza il codice senza eseguirlo: è il primo filtro della classificazione richiesta.
- In quattro casi il modello ha incapsulato l'output in un blocco markdown nonostante il divieto esplicito. La frequenza di questi scostamenti è una misura di aderenza al formato.
- Tempo medio per generazione: 5,5 secondi, tutte riuscite al primo tentativo.

Confronto qualitativo preliminare: sullo stesso campione, il modello 70B ha prodotto l'import corretto e nessun markdown; il modello 1B, in una prova preliminare eseguita in locale, ha ignorato l'istruzione sull'import ricadendo su `import pytest` — file che non sarebbe eseguibile. È il gradiente che lo studio intende quantificare.

## 5. Esecuzione dei test e prime misure (8B, 100 campioni)

Procedura: per ogni file generato, controllo sintattico con `ast.parse`; se supera, esecuzione con pytest in una cartella temporanea isolata, con timeout, accanto a un file `funzione.py` contenente la funzione sotto test; infine calcolo della coverage con `coverage.py` sulla sola funzione.

| esito | campioni |
|---|---|
| tutti i test passano | 3 |
| eseguibile, ma almeno un test fallisce | 88 |
| non eseguibile | 9 |
| timeout | 0 |

- Coverage media **77,4%** sui 91 campioni eseguibili (mediana 87,5%).
- Coverage media **70,4%** considerando tutti i 100 campioni e attribuendo 0% ai non eseguibili.
- Degli 800 test generati complessivamente, ne passano **187 (23,4%)**.

**Denominatore della coverage.** Le due medie rispondono a domande diverse e vanno riportate entrambe: quella sui soli eseguibili risponde a "quando il file funziona, quanta parte della funzione viene esercitata?", quella su tutti i campioni risponde a "quanto copre il modello complessivamente?". Indicare sempre quale denominatore si sta usando.

**Coverage alta e correttezza bassa.** Il divario tra 77,4% di copertura e 23,4% di test corretti è il risultato più significativo: il modello sceglie input plausibili e li fa arrivare al codice — perciò le righe risultano eseguite — ma sbaglia quasi sempre il valore atteso nell'assert. Va sottolineato che la coverage è alta *anche grazie ai test che falliscono*: un assert sbagliato esegue comunque la funzione prima di fallire. Le due metriche vanno quindi lette insieme. È lo stesso fenomeno che TestGenEval attribuisce alla difficoltà dei modelli nel ragionare sull'esecuzione.

**Artefatto corretto: import mancanti.** Il campo `code` del dataset non include gli import necessari alla funzione (per esempio `re` in `fix_labels`), che quindi solleva `NameError` a tempo di esecuzione. Senza correzione, test perfettamente sensati risultavano falliti per un motivo estraneo al modello. Si antepone perciò alla funzione un preambolo con gli import di libreria standard, escluso dal calcolo della coverage tramite `# pragma: no cover`. L'effetto è misurabile: i test corretti passano dal 20,2% al 23,4% e la coverage media dal 72,4% al 77,4%.

**Il campo `test_list` non è ground truth.** Gli assert umani contenuti nel dataset passano solo nel 12% dei casi sul codice fornito. La documentazione di UnLeakedTestBench chiarisce il motivo: gli autori dichiarano esplicitamente di **non** rilasciare i test di riferimento, per non farli entrare nei dati di addestramento dei modelli futuri. Il campo `test_list` è un residuo dello schema del dataset di origine e non può essere usato come riferimento; per esempio, per `is_degree_in_degree_range(30, 150, 100)` l'assert si attende `True` mentre il codice fornito restituisce `False`.

**Confronto con i risultati pubblicati.** Il paper di UnLeakedTestBench (arXiv:2508.00408) riporta, come media su 12 modelli di dimensioni maggiori e in gran parte specializzati sul codice, Pass@1 del 41,32% e copertura di riga del 45,10%. Il 23,4% di test corretti ottenuto qui con un modello generalista da 8B è coerente con quel quadro. La coverage misurata risulta invece più alta, ma non è direttamente confrontabile: qui viene conteggiata anche l'esecuzione prodotta dai test che falliscono, e le funzioni sono i primi 100 campioni di ULT_Lite anziché l'intero benchmark.

## 6. Nota metodologica: disponibilità del servizio

Durante la prima sessione di lavoro tutte le richieste di inferenza verso i tre modelli andavano in timeout, mentre l'endpoint di elenco dei modelli rispondeva regolarmente e il modello da 70B era raggiungibile. Le prove condotte hanno escluso come cause: chiave e connessione, il codice client (stesso esito con lo script fornito dalla relatrice), la rete (stesso comportamento da rete fissa e da hotspot), la temperatura, il numero massimo di token, la lunghezza del prompt e l'uso dello streaming. Una richiesta identica a una riuscita pochi minuti prima falliva. In una sessione successiva, senza alcuna modifica, tutte le richieste sono passate al primo tentativo. Si tratta quindi di disponibilità intermittente degli endpoint: lo script prevede fino a sei tentativi per campione.

## 7. Lavoro preliminare (prima della definizione dell'impianto)

Questa fase non fa parte dell'esperimento finale ma ne ha informato la costruzione; il codice si trova in `preliminare/`.

- **Libreria `ast`**: estrazione di un riassunto strutturale di un file Python (nome e argomenti delle funzioni, docstring, numero di `return` e di `if`, eccezioni sollevate, righe di inizio e fine). Il numero di rami è legato al numero di cammini da coprire; `lineno`/`end_lineno` permettono di mappare le righe non coperte alla funzione corrispondente.
- **Klara**: generazione automatica di scheletri di test tramite il solver SMT Z3. Su funzioni semplici individua da sé i valori di confine (per una classificazione di voti: 0, 18, 24, 28). Limite rilevante: supporta un sottoinsieme ristretto di Python e non è installabile su Python 3.12.
- **Ciclo manuale con LLM**: generando test via chat e restituendo al modello le righe non coperte, la coverage di un file di esempio è passata dal 47% al 100% in una sola iterazione. Su funzioni semplici però il risultato è quasi garantito e non dimostra nulla: serve codice dove il primo tentativo fallisce.
- **Codice irraggiungibile**: su un file di prova più complesso, l'unica riga non coperta dopo 46 test si è rivelata irraggiungibile per costruzione (codice difensivo mai attivabile). Ne segue che un criterio di arresto basato sul raggiungimento del 100% non è praticabile, e che le righe non coperte hanno anche un valore diagnostico.
