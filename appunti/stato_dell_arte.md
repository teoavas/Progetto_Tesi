# Stato dell'arte — struttura proposta

Tesi: **Metriche per Valutare la Qualità degli Unit Test Generati con i Large Language Models**

Il capitolo non riassume i paper uno per uno: li usa come mattoni di un discorso che porta al problema della tesi. Il filo conduttore è **la misura**: si parte da cosa rende buono un test, si mostra come la ricerca ha provato a generarli automaticamente, e si arriva alla domanda "con quali metriche giudichiamo i test prodotti da un LLM, e quali mancano?".

---

## 2.1 Il testing di unità e il costo della scrittura manuale

Cosa contiene:

- Ruolo degli unit test: individuare le incongruenze fra specifica e implementazione, catturare regressioni. Correggere un difetto in fase iniziale costa molto meno che scoprirlo alla fine.
- Il collo di bottiglia: scrivere test è lento, ripetitivo e spesso trascurato. È la motivazione condivisa da tutti i lavori del settore.
- **Cosa vuol dire "test di qualità"**: qui si anticipa la struttura del capitolo — un test deve essere corretto ed eseguibile, deve esercitare il codice, deve saper distinguere il codice giusto da quello sbagliato, e deve restare leggibile e manutenibile. Sono le quattro famiglie di metriche della sezione 2.5.

Fonti: introduzioni di [1], [2], [15] (tutte e tre aprono così).

---

## 2.2 La generazione automatica di test prima degli LLM

Cosa contiene:

- **Approcci search-based**: EvoSuite per Java [8], Pynguin per Python [9]. Cercano input che massimizzano la copertura tramite algoritmi evolutivi.
- **Approcci simbolici**: esecuzione simbolica [10] e solver di vincoli (Z3 [11]) per derivare input che raggiungono cammini specifici. È la famiglia a cui appartiene Klara, con cui hai fatto le prove preliminari: su una funzione a soglie trovava da sola i valori di confine.
- **Il limite comune**: questi strumenti producono test poco leggibili, e soprattutto non hanno un *oracolo*. Sanno raggiungere una riga, ma il valore atteso lo ricavano eseguendo il codice così com'è: fotografano il comportamento attuale invece di verificare quello desiderato.

Perché sta qui: introduce la distinzione **raggiungere il codice** vs **sapere cosa deve restituire**, che è esattamente il divario coverage/correttezza che i tuoi dati mostrano.

Fonti: EvoSuite [8], Pynguin [9], esecuzione simbolica [10], solver Z3 [11], sezione "related work" di [15].

---

## 2.3 La generazione di test con i Large Language Models

Cosa contiene:

- **Il salto rispetto al passato**: gli LLM producono test che assomigliano a quelli scritti dagli sviluppatori, con nomi parlanti e assert espressi in termini di comportamento atteso. Primi lavori: modelli addestrati a generare assert — ATLAS [13] e TOGA [14].
- **TestPilot** [15] (Schäfer et al., IEEE TSE 2024): genera test senza addestramento né few-shot, costruendo il prompt con firma, documentazione ed esempi d'uso della funzione. Raggiunge il 70,2% di copertura di istruzioni mediana su pacchetti npm, contro il 51,3% dello stato dell'arte precedente. Introduce l'analisi delle **assert non banali**, cioè quelle che verificano davvero il comportamento del modulo sotto test.
- **Approcci iterativi e ibridi**: TestART [20] (generazione e riparazione co-evolutive), ChatTester [18], ChatUniTest [19], CoverUp [17] (guidato dalle righe non coperte, su Python) e CodaMOSA [16] (l'LLM sblocca la ricerca quando si arena). Per una visione d'insieme: le rassegne [21] e [22]. Va citato perché è la direzione naturale del campo, ma la tua tesi resta volutamente a colpo singolo.
- **Il caso dei linguaggi a tipizzazione dinamica**: in Python mancano i tipi statici che guidano gli strumenti tradizionali, e questo rende il compito diverso da Java.

Nota su TestPilot: lavora su **JavaScript**, non su Python — è probabilmente il paper che ti sembrava meno inerente. In realtà è centrale per la tua tesi, non per il linguaggio ma per il metodo: è il lavoro che definisce come si costruisce il prompt e, soprattutto, che introduce metriche di qualità oltre la copertura. Il suo diagramma di flusso prompt → test è ottimo anche per il capitolo sul tuo sistema.

---

## 2.4 I benchmark per valutare la generazione di test

Cosa contiene: il confronto fra i banchi di prova esistenti, con una tabella.

| benchmark | granularità | linguaggio | dimensione | metriche | decontaminazione |
|---|---|---|---|---|---|
| TestEval [2] | programma singolo (LeetCode) | Python | 210 programmi | copertura complessiva, di riga/ramo mirata, di cammino mirata | no |
| TestGenEval [3] | file | Python | 1.210 coppie codice-test | pass@k, coverage, mutation score | no |
| UnLeakedTestBench (ULT) [1] | funzione | Python | 3.909 funzioni | Pass@k, LCov@k / BCov@k, Mut@k | sì |
| SWT-Bench [4] | modifica di repository | Python | 1.762 casi | pass@k | no |

Punti da sviluppare:

- **Granularità**: molti benchmark valutano a livello di file o classe; ULT porta la valutazione a livello di funzione, che è l'unità naturale dello unit testing.
- **Realismo**: il codice di LeetCode è autoconsistente e artificiale, e gonfia i risultati; ULT attinge a The Stack v2 [7] (codice reale) e tiene solo funzioni con complessità ciclomatica ≥ 10, escludendo i casi banali.
- **Contaminazione dei dati**: è il problema più grave. Se le funzioni e i loro test erano nei dati di addestramento, il modello sta ricordando, non generalizzando. ULT filtra le funzioni con test pubblicamente disponibili; PreLeakedTestBench (PLT) è il sovrainsieme che le include, e serve proprio a misurare l'effetto della contaminazione per differenza. Gli autori mostrano che le prestazioni su ULT correlano con l'abilità di scrittura di codice del modello, mentre su dati contaminati sono gonfiate dalla memorizzazione, soprattutto nella copertura dei rami.
- **Complessità ciclomatica** [12]: V = e − n + p sul grafo di controllo di flusso. Più è alta, più decisioni e cammini di esecuzione ci sono. La soglia ≥ 10 è il criterio con cui ULT garantisce funzioni non banali.
- **Divario fra benchmark**: sullo stesso compito, i modelli passano dal 91,79% di Pass@1 su TestEval al 41,32% su ULT. Il salto dice quanto pesa la scelta del banco di prova.

Qui va dichiarato che il tuo lavoro usa ULT, e perché: livello di funzione, codice reale, e nessun rischio di contaminazione.

---

## 2.5 Metriche per la qualità dei test *(il cuore del capitolo)*

Questa è la sezione che giustifica il titolo della tesi. Ogni sottosezione: cosa misura, come si calcola, cosa non vede.

### 2.5.1 Correttezza ed eseguibilità

- **Pass@k** [5]: proporzione di test corretti, cioè che compilano, arrivano a termine e le cui assert esprimono aspettative valide. La metrica nasce nella valutazione dei modelli per la generazione di codice [5, 6] ed è adottata da tutti i benchmark di test [1, 2, 3].
- Livelli di fallimento da distinguere: codice sintatticamente non valido (verificabile con un parser AST, senza eseguire nulla), codice che non arriva all'esecuzione (import mancanti, errori di raccolta), test eseguiti che falliscono.
- Perché la distinzione conta: un file non eseguibile e un test che fallisce dicono cose diverse sul modello — il primo è un errore di forma, il secondo un errore di ragionamento.

### 2.5.2 Copertura del codice

- Copertura di istruzioni (LCov) e di ramo (BCov); copertura di cammino nei casi mirati; ΔCov come guadagno incrementale.
- La copertura di ramo è più severa e, secondo [1], è anche quella più sensibile alla contaminazione dei dati.
- Attenzione al denominatore: media sui soli file eseguibili o su tutti i campioni? Sono due domande diverse e vanno dichiarate entrambe.

### 2.5.3 Capacità di rilevare difetti

- **Mutation score** (Mut@k) [25]: si iniettano difetti sintetici nel codice e si misura quanti vengono scoperti dai test. Strumento usato da ULT: Cosmic Ray per Python [33]. La validità dei mutanti come sostituti dei difetti reali è argomentata in [24].
- È la metrica più difficile da ingannare: per uccidere un mutante il test deve distinguere il codice sano da quello guasto, quindi deve avere un oracolo corretto e non solo passare per la riga giusta.

### 2.5.4 I limiti della copertura come indicatore

- Inozemtseva & Holmes [23], *Coverage Is Not Strongly Correlated with Test Suite Effectiveness* (ICSE 2014): controllando il numero di test nella suite, la correlazione fra copertura ed efficacia scende a bassa o moderata; la dimensione della suite è un fattore confondente.
- Studio di replicabilità recente sui test generati da LLM [26]: riporta la stessa domanda sulle suite prodotte dai modelli.
- Conseguenza per la tesi: la copertura da sola è un indicatore parziale, e per questo servono metriche affiancate. È l'argomento che motiva l'intero lavoro.

### 2.5.5 Qualità del codice di test

- **Test smell**: difetti ricorrenti di progettazione dei test. Su test generati da LLM prevalgono *Assertion Roulette* (molte assert in un test, senza messaggi, e non si capisce quale abbia fallito) e *Magic Number Test* (numeri sparsi nel codice senza spiegazione). Il concetto di test smell è introdotto in [27]; l'analisi su test generati da LLM è in [28].
- **Leggibilità e manutenibilità**: i test da LLM sono più leggibili di quelli generati dagli strumenti search-based, ma restano meno curati di quelli umani.
- **Duplicazione e ridondanza**: quante righe si ripetono fra i test generati. Un modello che produce dieci varianti dello stesso caso gonfia i numeri senza aggiungere valore.
- **Assert non banali** (da TestPilot [15]): assert che verificano davvero il comportamento, contro assert vuote o tautologiche.

### 2.5.6 Metriche sul comportamento del modello

Non sono metriche sui test ma sul processo, e raccontano molto sui modelli piccoli:

- Aderenza al formato richiesto (rispetto dei vincoli del prompt: import, numero di test, assenza di markdown).
- Troncamento della risposta per esaurimento del budget di token.
- Tempo per generazione e costo.

---

## 2.6 Sintesi e posizionamento del lavoro

Cosa contiene: la sintesi che apre la strada ai capitoli successivi.

Lacune individuate nella letteratura:

1. **I modelli valutati sono quasi sempre grandi o specializzati sul codice.** ULT [1] valuta 12 modelli fra cui DeepSeekCoder, Qwen2.5-Coder, Gemma-3, Phi-4; i modelli generalisti molto piccoli (1-8 miliardi di parametri) sono poco esplorati, benché siano gli unici eseguibili su una macchina ordinaria.
2. **Le metriche vengono riportate in parallelo, ma raramente messe in tensione fra loro.** Il divario fra copertura alta e correttezza bassa è il fenomeno più interessante e merita di essere misurato esplicitamente.
3. **Alcune dimensioni restano fuori dai benchmark**: la ridondanza fra i test generati, il numero di volte in cui la stessa riga viene rieseguita, l'aderenza al formato richiesto.

Contributo della tesi: valutare tre modelli di taglia crescente a parità di prompt, dataset e parametri, aggiungendo alle metriche classiche (esito, copertura) misure di ridondanza e di comportamento, e discutendo cosa ciascuna metrica vede e cosa nasconde.

---

## Bibliografia

L'elenco completo e numerato è in `bibliografia.md`, con l'indicazione di cosa citare per ogni tema. Per Overleaf: `references.bib`, da richiamare con `\cite{chiave}`.

I quattro PDF già in `paper/` corrispondono a [1] UnLeakedTestBench, [2] TestEval, [15] TestPilot, più i tuoi appunti di lettura.

---

## Metriche aggiuntive proponibili per il tuo lavoro

Oltre alle tre di ULT (Pass@k, LCov/BCov, Mut@k), candidate concrete e già misurabili con quello che hai:

| metrica | cosa misura | come si calcola |
|---|---|---|
| ridondanza fra i test | quanti test esercitano lo stesso cammino | conteggio delle esecuzioni per riga: righe attraversate molte volte segnalano test sovrapposti |
| duplicazione testuale | quanto codice di test è ripetuto | strumenti di rilevazione dei cloni sui file di test |
| aderenza al formato | quanto il modello rispetta i vincoli del prompt | percentuale di risposte conformi (import corretto, niente markdown, numero di test nel range) |
| tasso di troncamento | quanto spesso il modello sfora il budget | `finish_reason = length` sul totale |
| densità di assert | assert per test, assert per riga coperta | conteggio sull'AST del file di test |
| divario copertura-correttezza | quanto il modello "tocca senza capire" | differenza fra copertura raggiunta e proporzione di test che passano |

L'ultima riga è la più interessante: non l'ho trovata come metrica dichiarata in letteratura, ed è esattamente ciò che i tuoi dati sull'8B mostrano.
