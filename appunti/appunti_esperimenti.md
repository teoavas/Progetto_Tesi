# Appunti di lavoro — generazione di unit test con LLM

*Note tenute durante il lavoro, da riadattare per le sezioni della tesi su Overleaf.*

## 1. Contesto e riferimento

Il riferimento è TestGenEval (ICLR 2025, https://openreview.net/pdf?id=7o6SG5gVev): un benchmark costruito su SWE-bench con 68.647 test da 1.210 coppie file codice-test, tratte da 11 repository Python reali. Valuta due compiti — generazione dell'intera test suite e completamento di una suite esistente — con metriche di esecuzione (pass@1, pass@5), coverage e mutation score, quest'ultimo ottenuto iniettando bug sintetici nel codice e misurando quanti vengono scoperti dai test.

Il risultato principale è che i modelli faticano sui progetti reali: il migliore (GPT-4o) si ferma a una coverage media del 35,2% e a un mutation score del 18,8%. La causa individuata dagli autori è la difficoltà dei modelli a ragionare sull'esecuzione del codice, con frequenti errori nelle assert sui cammini complessi.

## 2. Oggetto di questa tesi

Misurare la qualità degli unit test generati da modelli di piccola taglia (Llama 1B, 3B, 8B) su funzioni Python reali, a parità di prompt e con temperatura 0.

Insieme definitivo delle metriche, concordato con la relatrice (sezione 9):

- **parte statica** — esito della generazione, validità sintattica, troncamento, aderenza ai vincoli del prompt, tempo di generazione;
- **parte dinamica** — esito dell'esecuzione (passato / eseguibile ma fallito / non eseguibile / timeout), Pass@1 sul singolo test, copertura di riga e di ramo, duplicazione, mutation score;
- **analisi dei fallimenti** — categorizzazione per causa, con esempi.

La riesecuzione delle righe, presente nelle prime versioni del piano, è uscita dall'insieme definitivo: `coverage.py` non la fornisce e servirebbe `sys.monitoring`. Va negli sviluppi futuri.

## 3. Impianto sperimentale

**Dataset.** UnLeakedTestBench, file `ULT_Lite.jsonl`: 200 campioni, uno per riga in formato JSON Lines. Ogni campione contiene il nome della funzione, il suo codice sorgente (funzione autonoma, eseguibile in isolamento), una descrizione in linguaggio naturale, un identificativo e una lista di assert scritti da umani. Si usano i primi 100 campioni nell'ordine del file. Le funzioni vanno da 8 a 171 righe, con mediana 34.

**Modelli.** `llama3.2:1b`, `llama3.2:3b` e `llama3.1:8b`, eseguiti **in locale con Ollama** attraverso un'interfaccia compatibile con la libreria `openai`. Sono gli stessi pesi rilasciati da Meta, qui quantizzati a 4 bit: la quantizzazione va dichiarata in tesi, e semmai penalizza il modello anziché favorirlo.

I primi cento campioni dell'8B erano stati generati su NVIDIA build prima del passaggio in locale (sezioni 4 e 5): quei dati restano archiviati come confronto fra piena precisione e quantizzazione, ma non fanno parte dello studio. Il modello da 70B è stato usato unicamente come controllo di funzionamento.

**Prompt.** Template fisso in tre sezioni. `[instruction]` elenca i vincoli: stile pytest senza classi, import esplicito della funzione sotto test, da 3 a 8 funzioni di test con nomi numerati, almeno un assert per test, divieto di riscrivere la funzione, divieto di spiegazioni e markdown. `[data]` contiene il solo codice della funzione (la descrizione in linguaggio naturale non viene passata). `[format]` mostra lo scheletro atteso dell'output: per i modelli piccoli, vedere la forma è più efficace che leggerne la descrizione.

**Parametri.** Temperatura 0, `max_tokens` 1024, una funzione per richiesta, output salvato in un file separato per ogni coppia (modello, campione).

## 4. Risultati preliminari — modello 8B su 100 campioni (NVIDIA, ARCHIVIATI)

> **Attenzione.** Questa sezione riguarda l'esecuzione su NVIDIA, che non fa più
> parte dello studio: è conservata come confronto fra piena precisione e
> quantizzazione. I dati correnti sono quelli locali della sezione 10, e su due
> punti **contraddicono** quanto scritto qui. Non riportare in tesi le
> osservazioni di questa sezione senza verificarle sui dati locali.

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

## 5. Esecuzione dei test e prime misure (8B, 100 campioni — NVIDIA, ARCHIVIATI)

> **Attenzione.** Anche questi numeri vengono dall'esecuzione su NVIDIA e non
> sono i dati dello studio. In particolare il divario 77,4% / 23,4% fra
> copertura e correttezza va ricalcolato in locale prima di comparire in tesi.
> Le osservazioni di metodo (denominatore della coverage, artefatto degli
> import mancanti, `test_list` non utilizzabile come riferimento) restano invece
> valide, perché non dipendono dall'infrastruttura.

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

## 6. Passaggio all'esecuzione in locale

Dopo il completamento dei 100 campioni con il modello 8B, gli endpoint di NVIDIA build hanno smesso di rispondere: prima sui tre modelli dello studio, poi anche sul 70B usato come controllo. La verifica è stata fatta con uno script ridotto all'osso (una richiesta di cinque token con contenuto "hi", senza tentativi né parametri personalizzati), che non ha ottenuto risposta. La generazione prosegue quindi in locale con Ollama, opzione già indicata come accettabile dalla relatrice.

**Corrispondenza dei modelli.** `llama3.2:1b`, `llama3.2:3b` e `llama3.1:8b` in Ollama sono gli stessi pesi rilasciati da Meta e serviti da NVIDIA. Cambia l'infrastruttura di esecuzione, non il modello. In locale i pesi sono quantizzati a 4 bit: la quantizzazione riduce la precisione numerica dei parametri per contenere l'occupazione di memoria, e tende semmai a peggiorare leggermente le prestazioni del modello — non a gonfiarle.

**Uniformità del confronto.** Per confrontare fra loro le tre taglie occorre che siano trattate allo stesso modo: i 100 campioni dell'8B verranno perciò rigenerati anche in locale. I risultati ottenuti su NVIDIA restano conservati e diventano un confronto secondario ma interessante — lo stesso modello, sullo stesso campione e con lo stesso prompt, a piena precisione e quantizzato.

**Parametri invariati.** Temperatura 0, `max_tokens` 1024, una funzione per richiesta, stesso template di prompt, stessa struttura dei file prodotti. Lo script di misura è il medesimo per entrambe le vie.

## 7. Nota metodologica: disponibilità del servizio

Durante la prima sessione di lavoro tutte le richieste di inferenza verso i tre modelli andavano in timeout, mentre l'endpoint di elenco dei modelli rispondeva regolarmente e il modello da 70B era raggiungibile. Le prove condotte hanno escluso come cause: chiave e connessione, il codice client (stesso esito con lo script fornito dalla relatrice), la rete (stesso comportamento da rete fissa e da hotspot), la temperatura, il numero massimo di token, la lunghezza del prompt e l'uso dello streaming. Una richiesta identica a una riuscita pochi minuti prima falliva. In una sessione successiva, senza alcuna modifica, tutte le richieste sono passate al primo tentativo. Si tratta quindi di disponibilità intermittente degli endpoint: lo script prevede fino a sei tentativi per campione.

## 8. Lavoro preliminare (prima della definizione dell'impianto)

Questa fase non fa parte dell'esperimento finale ma ne ha informato la costruzione; il codice si trova in `preliminare/`.

- **Libreria `ast`**: estrazione di un riassunto strutturale di un file Python (nome e argomenti delle funzioni, docstring, numero di `return` e di `if`, eccezioni sollevate, righe di inizio e fine). Il numero di rami è legato al numero di cammini da coprire; `lineno`/`end_lineno` permettono di mappare le righe non coperte alla funzione corrispondente.
- **Klara**: generazione automatica di scheletri di test tramite il solver SMT Z3. Su funzioni semplici individua da sé i valori di confine (per una classificazione di voti: 0, 18, 24, 28). Limite rilevante: supporta un sottoinsieme ristretto di Python e non è installabile su Python 3.12.
- **Ciclo manuale con LLM**: generando test via chat e restituendo al modello le righe non coperte, la coverage di un file di esempio è passata dal 47% al 100% in una sola iterazione. Su funzioni semplici però il risultato è quasi garantito e non dimostra nulla: serve codice dove il primo tentativo fallisce.
- **Codice irraggiungibile**: su un file di prova più complesso, l'unica riga non coperta dopo 46 test si è rivelata irraggiungibile per costruzione (codice difensivo mai attivabile). Ne segue che un criterio di arresto basato sul raggiungimento del 100% non è praticabile, e che le righe non coperte hanno anche un valore diagnostico.

## 9. Piano di misura concordato con la relatrice (agosto 2026)

Indicazioni ricevute per email, integrate con gli appunti presi a voce.

### 9.1 L'albero di classificazione

È la struttura portante dei capitoli 3 e 4, e va disegnata come figura nella tesi.

```
N campioni
├─ test NON scritti                    (parte statica: fallimento della pipeline)
│     nessuna risposta, risposta vuota, errore dell'endpoint
└─ test SCRITTI
      ├─ sintatticamente non validi    (parte statica: ast.parse fallisce)
      └─ sintatticamente validi
            ├─ FALLITI                 (parte dinamica: almeno un test non passa)
            │     da raggruppare per categoria di fallimento
            └─ PASSATI                 (parte dinamica: tutti i test passano)
```

Il taglio statico/dinamico coincide con quello fra ciò che si stabilisce senza eseguire nulla (`ast.parse`, `finish_reason`, aderenza al formato) e ciò che richiede l'esecuzione. Ogni ramo si riporta come **percentuale**, e **separatamente per ogni modello**.

### 9.2 Metriche da calcolare

Insieme definitivo, tutte in percentuale per renderle indipendenti dal setup:

| metrica | denominatore | stato |
|---|---|---|
| esiti dell'albero (§9.1) | campioni del modello | parziale: da separare "non scritti" da "non eseguibili" |
| copertura di riga | righe eseguibili della funzione | fatta |
| copertura di ramo | rami della funzione | **da aggiungere**: `coverage run --branch` |
| duplicazione | righe di test duplicate su righe di test totali | da scrivere |
| aderenza al formato | campioni del modello | da scrivere |
| mutation score | mutanti non equivalenti uccisi | da scrivere (Cosmic Ray, su un sottoinsieme) |
| tempo di generazione | — | già in `generazioni.csv`, da unire |

Escluse d'accordo con la relatrice: accuratezza semantica delle assert, perché richiede analisi umana.

### 9.3 Punti da chiarire con la relatrice

1. **"Coverage e duplicazione sui test che hanno successo".** Se "successo" significa il *file* intero, sull'8B il campione si riduce a 3 casi su 100 e la misura non dice nulla. Se significa la *singola funzione di test* — lettura coerente con il Pass@k di ULT, che conta i test corretti e non i file — allora la base è ampia (187 test su 800) e la misura ha senso. Proposta operativa: rieseguire la suite deselezionando i test che falliscono e misurare copertura e duplicazione su quel sottoinsieme, riportando comunque anche il valore su tutti i test.
   Motivo per riportare entrambi: la copertura è alta **anche grazie** ai test che falliscono, perché un assert sbagliato esegue comunque la funzione prima di fallire. Restringersi ai soli test passati cancella il risultato più interessante del lavoro (77,4% di copertura contro 23,4% di test corretti).
2. **"Aderenza al formato (explicit typing)".** Il template del prompt non chiede annotazioni di tipo: i vincoli verificabili sono stile pytest senza classi, import `from funzione import ...`, da 3 a 8 test con nomi numerati, almeno un assert per test, assenza di markdown. Da chiedere se intendeva altro.
3. **"Imitation score".** Termine non standard. L'interpretazione più probabile è la somiglianza fra test generati e test umani, misurata in TestPilot \cite{schaefer2024testpilot} con la distanza di edit normalizzata (il 92,8% dei test generati ha meno del 50% di somiglianza con quelli esistenti). Così definita è automatizzabile; da confermare.
4. **Tempo di generazione.** Misurabile, ma confrontabile solo a parità di infrastruttura: sull'8B si passa da ~3 secondi su NVIDIA a ~29-79 secondi in locale con pesi quantizzati. Il confronto fra le tre taglie va fatto solo sui dati locali.

### 9.4 Modifiche necessarie a `misura.py`

- salvare l'output integrale di pytest per ogni campione (`report/<sigla>/<indice>.txt`): serve per l'analisi dei fallimenti e la loro categorizzazione;
- distinguere "non scritto" (file assente o vuoto) da "sintatticamente non valido";
- aggiungere `--branch` al comando di coverage;
- contare le funzioni di test presenti nel file tramite AST, per avere il denominatore per campione;
- unire il tempo di generazione da `generazioni.csv`.

### 9.5 Cosa non misuriamo

Va nella sezione dei lavori correlati (il capitolo 2, lo stato dell'arte) e ripreso negli sviluppi futuri: test smell, leggibilità, assert non banali, ridondanza misurata come riesecuzione delle righe se non si arriva a implementarla.


## 10. Misure statiche in locale sui tre modelli (settembre 2026)

Prodotte da `locale/statiche.py`, che scrive `locale/statiche.csv`: una riga per
campione per modello, 300 righe. Nessuna esecuzione dei test: solo `ast.parse`,
analisi dell'albero sintattico e il registro `generazioni.csv`. Cento campioni
per ciascuno dei tre modelli, nessuno mancante.

| | 1B | 3B | 8B |
|---|---|---|---|
| scritti | 100% | 100% | 100% |
| sintatticamente validi | 92,0% | 99,0% | 94,0% |
| risposte troncate | 5,0% | 0% | 6,0% |
| import corretto | 23,9% | 100% | 100% |
| da 3 a 8 test | 93,5% | 100% | 98,9% |
| nomi conformi | 95,7% | 99,0% | 100% |
| un assert per test | 89,1% | 80,8% | 97,9% |
| un oracolo per test | 98,9% | 100% | 100% |
| **tutti i vincoli** | **21,7%** | **79,8%** | **96,8%** |
| test per file (media) | 7,6 | 7,1 | 7,2 |
| tempo medio | 24,2 s | 37,2 s | 90,8 s |

Le percentuali di aderenza sono calcolate sui soli file sintatticamente validi.

**Nessun fallimento della pipeline.** Tutti e trecento i campioni hanno prodotto
un file. Il primo ramo dell'albero e' quindi vuoto, ed e' un risultato da
riportare come tale.

Nella prima esecuzione otto campioni risultavano falliti (indici 44 e 99 su
tutti e tre i modelli, 45 su 3B e 8B). La causa non era il modello ma lo script:
quei campioni sono fra i pochi del dataset con caratteri non ASCII — giapponese
nel 44 e nel 99, una freccia nel 45 — che il modello riproduce nelle proprie
asserzioni. Su Windows la console usa cp1252 e il `print` della risposta
sollevava `UnicodeEncodeError`, facendo uscire `genera.py` con codice di errore.
Risolto forzando UTF-8 sullo standard output. Da allora `genera_tutti.py`
stampa anche il messaggio di errore, cosi' un fallimento non resta muto.
E' un artefatto da menzionare in tesi fra le minacce alla validita': senza la
correzione, tre funzioni sarebbero state escluse dal confronto per una ragione
estranea ai modelli.

**L'import e' una soglia, non un gradiente.** Il 1B rispetta l'istruzione
sull'import solo nel 23,9% dei casi e ripiega su `import pytest`; il 3B e l'8B
la rispettano sempre. Fra uno e tre miliardi di parametri non c'e' un
miglioramento progressivo ma un salto netto. E' anche il componente che
determina da solo il totale del 1B: gli altri tre vincoli stanno sopra l'89%.

**L'aderenza complessiva e' invece un gradiente pulito**: 21,7% -> 79,8% -> 96,8%.

**Assert e oracolo vanno letti insieme.** Il valore basso del 3B sull'assert
(80,8%) non indica test privi di verifica: i casi sono blocchi `pytest.raises`,
che verificano il sollevamento di un'eccezione. Alla lettera violano il vincolo
del prompt, ma un oracolo ce l'hanno — infatti la riga "un oracolo per test" da'
100%. Le due colonne misurano cose diverse: obbedienza al prompt la prima,
presenza di un oracolo la seconda.

**Correzione rispetto alla sezione 4 (NVIDIA).** Due affermazioni riportate li'
non valgono sui dati locali:

- *"Tutti i casi di codice non valido derivano dal troncamento"*: falso in
  locale. Il 1B produce file non validi non troncati (parentesi non chiuse, un
  blocco markdown non terminato) e il 3B uno.
- *"Alcuni campioni troncati superano comunque il controllo sintattico"*: in
  locale non accade. Troncamento e invalidita' sintattica coincidono sempre.

**Il troncamento non segue la taglia**: 5,0% sul 1B, 0% sul 3B, 6,0% sull'8B.
La validita' sintattica lo rispecchia, essendo i file non validi in gran parte
troncati. E' un'anomalia da approfondire, non un errore di misura.

**I modelli scelgono sempre il massimo consentito.** La grande maggioranza dei
file validi contiene 7 o 8 test: quasi nessuno ne scrive 3, 4 o 5, pur essendo
ammesso dal prompt. Rispettano il vincolo scegliendone sistematicamente
l'estremo superiore.

**Vincoli non misurati come statistica**, perche' osservati in pochissimi casi;
vanno usati come esempi nella categorizzazione dei fallimenti:

- *niente classi*: violato in 2 file, entrambi del 1B (indici 32 e 52).
- *niente markdown*: non misurabile in generale, perche' `genera.py` applica
  `pulisci()` prima di salvare. Sopravvive solo nei blocchi malformati: un caso
  sul 1B (indice 78), dove il blocco non era chiuso e la regex non l'ha colto.

**Anomalie singole utili come esempi**: il campione 16 del 1B contiene un solo
test seguito dalla riga `test_next_holiday_2.py`, cioe' un nome di file scritto
come se fosse codice; il campione 95 del 1B ne contiene 25, con nomi che non
seguono lo schema richiesto.

## 11. Misure dinamiche in locale sui tre modelli (settembre 2026)

Prodotte da `locale/misura.py`, che esegue ogni file di test con pytest in una
cartella isolata accanto alla funzione sotto test e scrive `misure_<sigla>.csv`.
Le tabelle si ottengono con `locale/riepilogo.py`, che unisce queste misure a
`statiche.csv` su `(modello, indice)`. L'output integrale di pytest e' salvato
in `locale/report/<sigla>/<indice>.txt` (escluso dal versionamento perche'
rigenerabile) ed e' la base della categorizzazione dei fallimenti.

### 11.1 Esiti

| esito | 1B | 3B | 8B |
|---|---|---|---|
| passato (tutti i test del file) | 0 | 2 | 2 |
| fallito | 83 | 96 | 91 |
| non eseguibile | 16 | 1 | 6 |
| timeout | 1 | 1 | 1 |

I 16 non eseguibili del 1B si scompongono in 8 errori di sintassi — gli stessi
rilevati nella parte statica — e 8 file che vengono analizzati ma si rompono
all'esecuzione.

**Il livello del file non e' utilizzabile.** I campioni in cui *tutti* i test
passano sono 0, 2 e 2 su cento. Qualunque metrica calcolata sui "file che hanno
successo" avrebbe una base di due campioni. La lettura per singolo test e'
l'unica praticabile, ed e' anche quella coerente con il Pass@k di ULT. Questo
risolve con i dati la prima domanda aperta con la relatrice.

I campioni con **almeno un** test passato sono invece 7, 45 e 56: e' questa la
base utilizzabile per le misure che richiedono test funzionanti, mutation score
compreso.

### 11.2 Correttezza e copertura

| | 1B | 3B | 8B |
|---|---|---|---|
| Pass@1 (sul singolo test) | 3,5% | 16,9% | 21,6% |
| test corretti / generati | 25/709 | 118/699 | 144/667 |
| copertura righe, tutti i campioni | 12,2% | 68,3% | 71,0% |
| copertura righe, soli eseguibili | 14,7% | 69,7% | 76,3% |
| copertura righe, solo con import corretto | 61,0% | 69,7% | 76,3% |
| copertura rami, soli eseguibili | 11,2% | 59,3% | 66,4% |

**Copertura alta e correttezza bassa, quantificate.** Sull'8B la copertura di
riga e' 76,3% mentre i test corretti sono il 21,6%. E' il risultato centrale
della tesi: i modelli raggiungono il codice e sbagliano il valore atteso.

**Replica del risultato su NVIDIA.** L'8B remoto dava 77,4% di copertura e 23,4%
di test corretti; in locale, con pesi quantizzati a 4 bit, da' 76,3% e 21,6%.
Il fenomeno non dipende dall'infrastruttura ne' dalla quantizzazione.

**Il crollo del 1B e' interamente l'import.** Sui campioni eseguibili copre il
14,7%, ma sui soli venti campioni in cui ha importato la funzione copre il
61,0%. Senza `from funzione import ...` la funzione non viene mai chiamata e la
copertura e' nulla per costruzione. Non e' un modello incapace di scrivere test:
e' un modello che non segue un'istruzione di una riga. Sul 3B e sull'8B le due
basi coincidono, perche' l'import e' sempre corretto.

**La copertura di rami sta sistematicamente sotto quella di riga**, di circa
dieci punti. E' la misura piu' severa, come atteso su funzioni con complessita'
ciclomatica non inferiore a dieci.

### 11.3 Duplicazione

| base | 1B | 3B | 8B |
|---|---|---|---|
| tutte le righe di test, campioni eseguibili | 13,6% | 3,7% | 25,3% |
| soli test passati, campioni con test passati | 10,7% | 0,7% | 8,9% |
| per confronto, tutte le righe sugli stessi campioni | 7,5% | 2,7% | 17,2% |

Definizione: quota di righe ripetute sul totale delle righe di test, ignorando
righe vuote e commenti; una riga presente n volte contribuisce n-1 ripetizioni.

**L'8B e' il piu' ridondante di tutti**, con 54 file su 93 sopra il 20% contro
5 su 98 del 3B. Il meccanismo e' la ripetizione della preparazione in ogni test:
nel campione 27 le righe `match = [0, 1, 2]`, `i = 1`, `m = 10` compaiono otto
volte identiche, una per funzione di test. E' il *Test Code Duplication* del
catalogo di van Deursen, quello che una fixture eliminerebbe.

**Cautela nell'interpretazione.** Il 3,7% del 3B non e' necessariamente un
merito: duplica poco perche' scrive test piu' scarni, spesso un solo assert
senza preparazione. La duplicazione non ordina i modelli da sola e va letta
insieme a quanto lavoro fa ciascun test.

**Attenzione al denominatore**, per lo stesso motivo visto con la copertura. La
duplicazione sui soli test passati va mediata sui soli campioni che ne hanno
almeno uno: includendo gli altri si sommano zeri strutturali e la media perde
significato (sul 1B si passa da 0,9% a 10,7%).

### 11.4 Categorizzazione dei fallimenti

Prodotta da `locale/fallimenti.py`, che legge i blocchi FAILURES dei report,
estrae il tipo di eccezione e il file in cui e' stata sollevata, e scrive
`fallimenti.csv` con una riga per test fallito (1788 in tutto).

| | 1B | 3B | 8B |
|---|---|---|---|
| test falliti analizzati | 684 | 581 | 523 |
| `AssertionError` | 21,5% | 71,1% | 81,8% |
| `NameError` | 72,2% | 9,0% | 4,4% |
| `TypeError` | 5,1% | 10,0% | 3,8% |
| **la funzione viene eseguita** (errore di oracolo) | **25,7%** | **88,6%** | **93,9%** |
| **la funzione non si raggiunge** (errore d'uso) | **74,3%** | **11,4%** | **6,1%** |

Criterio delle due famiglie: il test ha esercitato la funzione se l'assert e'
fallito, se attendeva un'eccezione che non e' arrivata, oppure se l'eccezione e'
nata dentro `funzione.py` — cioe' la funzione e' stata chiamata ed e' stata lei
a rifiutare l'input. Negli altri casi il test non e' arrivato a chiamarla.

**Crescendo, il modello non fallisce di meno: fallisce in modo diverso.** Il 1B
sbaglia a livello meccanico e non tocca la funzione in tre casi su quattro. Il
3B e l'8B seguono le istruzioni e vanno a sbattere contro l'ostacolo successivo,
che e' l'oracolo. E' la verifica empirica della distinzione fra raggiungere il
codice e sapere cosa deve restituire, introdotta nella sezione 2.2 della tesi.

Spiega anche perche' la copertura resta alta mentre la correttezza crolla: nel
93,9% dei fallimenti dell'8B la funzione viene comunque eseguita, e le sue righe
risultano quindi coperte.

### 11.5 Cosa manca

Il mutation score e' l'unica metrica non ancora calcolata. Richiede suite che
passino sul codice sano, quindi va calcolato restringendo ogni file ai soli test
che passano: la base utile e' di 45 campioni sul 3B e 56 sull'8B, mentre sul 1B
si ferma a 7 — troppo pochi, ed e' esso stesso un risultato da riportare.
