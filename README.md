# Progetto tesi — Valutazione della generazione di unit test con LLM

Tesi triennale di Matteo Savastano — Università degli Studi di Cagliari.

## Obiettivo

Misurare la qualità degli unit test generati da modelli linguistici di piccola taglia (Llama 1B, 3B, 8B) su funzioni Python reali, a parità di prompt e con temperatura 0.

Metriche misurate:

- **coverage** del codice sotto test
- **ripetizione delle righe**: quante volte ogni riga viene rieseguita
- **duplicazione** tra i file di test generati
- **esito**: test passato / eseguibile ma fallito / non eseguibile

Dataset: [UnLeakedTestBench](https://github.com/huangd1999/UnLeakedTestBench) (`ULT_Lite.jsonl`), 20 campioni, obiettivo 100.

## Struttura

```
benchmark/              lavoro principale
├── dataset/            ULT_Lite.jsonl + campioni selezionati
├── prompts/            prompt inviati, uno per campione e modello
├── generated/          output dei modelli (grezzo + codice ripulito)
├── results/            registro delle generazioni, metriche, grafici
├── carica_dataset.py   selezione dei campioni
├── prompt.py           costruzione del prompt e pulizia dell'output
├── prompt_template.txt il template dichiarato ([instruction]/[data]/[format])
└── genera.py           chiamate ai modelli, salvataggio, tempi

latex/                  scheletro della tesi (capitoli in .tex)
appunti/                note di lavoro
preliminare/            lavoro esplorativo iniziale (ast, Klara, loop manuale)
```

## Come eseguire

```bash
pip install -r requirements.txt

# 1. scaricare ULT_Lite.jsonl in benchmark/dataset/
# 2. selezionare i campioni
python benchmark/carica_dataset.py

# 3. impostare la chiave API (mai scriverla nei file!)
#    PowerShell:  $env:NVIDIA_API_KEY = "nvapi-..."

# 4. generare (prova rapida su 3 campioni con un modello)
python benchmark/genera.py --modello 1b --limite 3
```
