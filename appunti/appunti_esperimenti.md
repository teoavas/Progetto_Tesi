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

## 5. Nota metodologica: disponibilità del servizio

Durante la prima sessione di lavoro tutte le richieste di inferenza verso i tre modelli andavano in timeout, mentre l'endpoint di elenco dei modelli rispondeva regolarmente e il modello da 70B era raggiungibile. Le prove condotte hanno escluso come cause: chiave e connessione, il codice client (stesso esito con lo script fornito dalla relatrice), la rete (stesso comportamento da rete fissa e da hotspot), la temperatura, il numero massimo di token, la lunghezza del prompt e l'uso dello streaming. Una richiesta identica a una riuscita pochi minuti prima falliva. In una sessione successiva, senza alcuna modifica, tutte le richieste sono passate al primo tentativo. Si tratta quindi di disponibilità intermittente degli endpoint: lo script prevede fino a sei tentativi per campione.

## 6. Lavoro preliminare (prima della definizione dell'impianto)

Questa fase non fa parte dell'esperimento finale ma ne ha informato la costruzione; il codice si trova in `preliminare/`.

- **Libreria `ast`**: estrazione di un riassunto strutturale di un file Python (nome e argomenti delle funzioni, docstring, numero di `return` e di `if`, eccezioni sollevate, righe di inizio e fine). Il numero di rami è legato al numero di cammini da coprire; `lineno`/`end_lineno` permettono di mappare le righe non coperte alla funzione corrispondente.
- **Klara**: generazione automatica di scheletri di test tramite il solver SMT Z3. Su funzioni semplici individua da sé i valori di confine (per una classificazione di voti: 0, 18, 24, 28). Limite rilevante: supporta un sottoinsieme ristretto di Python e non è installabile su Python 3.12.
- **Ciclo manuale con LLM**: generando test via chat e restituendo al modello le righe non coperte, la coverage di un file di esempio è passata dal 47% al 100% in una sola iterazione. Su funzioni semplici però il risultato è quasi garantito e non dimostra nulla: serve codice dove il primo tentativo fallisce.
- **Codice irraggiungibile**: su un file di prova più complesso, l'unica riga non coperta dopo 46 test si è rivelata irraggiungibile per costruzione (codice difensivo mai attivabile). Ne segue che un criterio di arresto basato sul raggiungimento del 100% non è praticabile, e che le righe non coperte hanno anche un valore diagnostico.
