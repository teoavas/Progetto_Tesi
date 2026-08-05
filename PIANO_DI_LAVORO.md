# Piano di lavoro — dopo l'incontro con la relatrice (4 agosto 2026)

## Specifica della relatrice (testo originale, da Overleaf)

```
% dataset (prendere 20 campioni, arrivare a 100 sarebbe l'ideale)
%   https://github.com/huangd1999/UnLeakedTestBench/blob/main/datasets/ULT_Lite.jsonl
% modelli da https://build.nvidia.com/models?filters=usecase%3Ausecase_code_gen
%   (prendere llama 1, 3, 8 billion)
% settare la temperatura a zero
% dichiarato il template per il prompt
% formattare il prompt
% [instruction] write the unit test for this function. Output only the code, formatted as ....
% [data] <sample del dataset>
%
% output viene salvato in file separati
% metriche da misurare
% - quanto sono in grado di coprire il codice effettivamente (coverage)
% - possibile misura di quanto sono rieseguite le linee (contare quante volte viene eseguita la stessa linea)
% - quante linee sono replicate (limitato ai file di test, per esempio con questo tool
%   https://github.com/platisd/duplicate-code-detection-tool)
% codice non eseguibile -> errori di python o simili OPPURE test falliti (sarebbe l'ideale distinguerli)
% - eseguibile ma fallito
% - non eseguibile
% aggiunge ulteriore valore fare la valutazione "senza LLM", ovvero con AST + KLARA
% si può mettere anche un esempio di generazione di test end-to-end e la spiegazione
%   delle metriche fatta per via visiva.
```

Priorità dichiarata: AST + Klara è **secondaria**, da affrontare solo dopo "il grosso".

## Cosa è il progetto ora

Uno **studio di misura**: si generano unit test con tre modelli Llama di taglie diverse, a temperatura 0 e con un prompt fisso, su un campione del dataset ULT; poi si misura la qualità dei test prodotti con un insieme di metriche. Non è (ancora) un sistema con ciclo di feedback: quello resta un possibile passo successivo.

## Il dataset ULT_Lite

Formato JSONL, un oggetto per riga. Campi verificati:

| campo | contenuto |
|---|---|
| `func_name` | nome della funzione, es. `is_degree_in_degree_range` |
| `code` | il codice sorgente della funzione (stringa, funzione autonoma) |
| `prompt` | descrizione in linguaggio naturale di cosa fa la funzione |
| `task_id` | identificativo del campione |
| `test_list` | assert di riferimento scritti da umani (gold tests) |

Note: le funzioni sono autonome (nessun import di progetto), quindi eseguibili in isolamento. Il campo `test_list` è utile come riferimento (baseline umana) per confrontare la coverage.

## Struttura prevista del codice

```
benchmark/
├── dataset/            ULT_Lite.jsonl + il sottoinsieme selezionato (20 campioni)
├── prompts/            prompt effettivamente inviati, uno per campione
├── generated/          output dei modelli, un file per (modello, campione)
├── results/            metriche in CSV/JSON + tabelle e grafici
├── carica_dataset.py   selezione dei campioni
├── genera.py           chiamate API a temperatura 0, salvataggio output
├── esegui.py           esecuzione dei test, classificazione degli esiti
└── metriche.py         coverage, conteggio esecuzioni per riga, duplicazione
```

La cartella `esperimenti/` resta come lavoro preliminare (pilota manuale, prove con ast e Klara).

## Roadmap 5 → 20 agosto

**5–6 ago — Dataset e impalcatura.** Scaricare `ULT_Lite.jsonl`, selezionare 20 campioni con criterio esplicito e riproducibile (es. i primi 20 per `task_id`, oppure campionamento casuale con seed fisso: da annotare, serve in tesi). Script di caricamento.

**6–7 ago — Accesso ai modelli e generazione.** Account su build.nvidia.com, chiave API, prima chiamata di prova. Definire il template del prompt (istruzione + dati + formato di output richiesto) e congelarlo: se cambia a metà, i risultati non sono confrontabili. Temperatura 0. Salvataggio degli output in file separati.

**8–10 ago — Esecuzione e classificazione degli esiti.** Eseguire ogni file di test generato in un processo isolato con timeout, e classificare in tre categorie: passato / eseguibile ma fallito / non eseguibile.

**11–13 ago — Metriche.** Coverage sulla funzione bersaglio; conteggio di quante volte ogni riga viene eseguita; duplicazione tra i file di test.

**14–16 ago — Aggregazione ed estensione.** Tabelle e grafici per modello e per metrica; se tutto regge, estendere da 20 a 100 campioni (a temperatura 0 basta una sola esecuzione per campione).

**17–19 ago — Scrittura.** Metodo, metriche e risultati su Overleaf. Esempio end-to-end di una generazione e spiegazione visiva delle metriche.

**20 ago — Riepilogo per la relatrice.**

**Dopo, se resta tempo:** valutazione "senza LLM" con AST + Klara come termine di paragone.

## Punti da chiarire con la relatrice

1. **Quali modelli esattamente**: "llama 1, 3, 8 billion" dovrebbe corrispondere a Llama 3.2 1B, Llama 3.2 3B e Llama 3.1 8B sul catalogo NVIDIA. Da confermare i nomi esatti prima di lanciare tutto.
2. **Cosa mettere nel prompt**: solo il `code` del campione, oppure anche il `prompt` in linguaggio naturale (la descrizione della funzione)? Sono due condizioni sperimentali diverse; forse vale la pena misurarle entrambe.
3. **Formato dell'output richiesto** ("formatted as ....", lasciato in sospeso nella specifica): blocco markdown ```python, oppure codice grezzo? Va deciso perché condiziona il parsing delle risposte.
4. **Criterio di selezione dei 20 campioni**: casuale con seed, oppure i primi N?
5. **Ruolo di `test_list`**: usarlo come baseline umana di riferimento per la coverage?

## Note tecniche già emerse

- **Conteggio delle esecuzioni per riga**: `coverage.py` registra solo se una riga è stata eseguita o no, non quante volte. Per contare le ripetizioni serve un tracciatore proprio (`sys.settrace`, o `sys.monitoring` su Python 3.12) che incrementi un contatore per riga.
- **Distinguere "non eseguibile" da "eseguibile ma fallito"**: controllo sintattico con `ast.parse` prima dell'esecuzione (se solleva `SyntaxError` → non eseguibile), poi codici di uscita di pytest (2 = errore di raccolta/import → non eseguibile; 1 = test eseguiti ma falliti; 0 = tutti passati).
- **Sicurezza**: il codice generato da un modello va eseguito in un processo separato con timeout, per evitare cicli infiniti o effetti indesiderati.
- **Riproducibilità**: a temperatura 0 l'output è deterministico, quindi una sola generazione per campione; annotare comunque data, nome esatto del modello e versione, perché i modelli sul catalogo possono cambiare.
