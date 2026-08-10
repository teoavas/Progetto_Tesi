# Piano di lavoro

## Cos'è il progetto

Uno studio di misura sulla generazione di unit test con LLM di piccola taglia. Si generano test con tre modelli Llama (1B, 3B, 8B) su 100 funzioni Python reali, a parità di prompt e con temperatura 0, e si misura la qualità dei test prodotti.

Specifica concordata con la relatrice (4 agosto 2026):

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

La parte AST + Klara è dichiarata secondaria: si affronta solo dopo il resto.

## Impianto sperimentale (parametri congelati)

- **Dataset**: ULT_Lite, 200 campioni; se ne usano i **primi 100 nell'ordine del file** (criterio deterministico, da dichiarare in tesi). Campi: `func_name`, `code`, `prompt` (descrizione naturale, **non** passata al modello), `task_id`, `test_list` (assert umani di riferimento).
- **Modelli**: `meta/llama-3.2-1b-instruct`, `meta/llama-3.2-3b-instruct`, `meta/llama-3.1-8b-instruct` su NVIDIA build. Il 70B è usato solo come controllo, fuori dallo studio.
- **Parametri**: temperatura 0, `max_tokens` 1024, una funzione per richiesta, prompt fisso a tre sezioni `[instruction]` / `[data]` / `[format]`.
- **Output**: un file per campione in `benchmark/generati/<modello>/`, più un registro `generazioni.csv` con `finish_reason`, numero di tentativi e secondi.

Cambiare uno di questi parametri obbliga a rigenerare tutti i campioni.

## Stato

| passo | stato |
|---|---|
| dataset e prompt | fatto |
| generazione 8B (100 campioni) | fatto |
| generazione 3B (100 campioni) | da fare |
| generazione 1B (100 campioni) | da fare |
| classificazione esiti (non eseguibile / fallito / passato) | da fare |
| coverage | da fare |
| ripetizione righe e duplicazione | da fare |
| tabelle, grafici e scrittura su Overleaf | da fare |
| valutazione senza LLM (AST + Klara) | opzionale, in coda |

## Prossimi passi

1. `python genera_tutti.py 3b 0 99` e poi `1b`.
2. Script di misura: per ogni file generato, controllo sintattico con `ast.parse`, esecuzione con pytest in processo isolato e con timeout, classificazione in *non eseguibile* / *eseguibile ma fallito* / *passato*.
3. Coverage della funzione sotto test; conteggio delle esecuzioni per riga (serve un tracciatore con `sys.settrace`/`sys.monitoring`: `coverage.py` registra solo se una riga è stata eseguita, non quante volte); duplicazione fra i file di test.
4. Aggregazione per modello, tabelle e grafici; esempio end-to-end e spiegazione visiva delle metriche.

## Note metodologiche da riportare in tesi

- **Disponibilità intermittente degli endpoint NVIDIA**: in una prima sessione tutte le richieste di inferenza andavano in timeout (con l'endpoint dei modelli funzionante e il 70B raggiungibile); in una sessione successiva, senza modifiche, tutte le richieste sono passate al primo tentativo. Lo script effettua fino a sei tentativi per campione.
- **Troncamento**: `finish_reason = length` va trattato come categoria a sé. Un file troncato può superare il controllo sintattico se il taglio cade a fine funzione, risultando sano ma incompleto.
- **Pulizia dell'output**: i modelli incapsulano il codice in blocchi markdown anche quando il prompt lo vieta; lo script li rimuove. La frequenza con cui accade è essa stessa una misura di aderenza al formato.

## Punti aperti per la relatrice

1. Le metriche di coverage: solo statement coverage o anche branch coverage?
2. Il campo `test_list` (assert umani) va usato come riferimento di confronto?
3. Il troncamento va contato tra i "non eseguibili" o riportato separatamente?
