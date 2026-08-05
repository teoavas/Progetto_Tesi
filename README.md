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
benchmark/
├── dataset/            ULT_Lite.jsonl
└── genera.py           legge un campione, chiama il modello, salva i test

latex/                  scheletro della tesi (capitoli in .tex)
appunti/                note di lavoro
preliminare/            lavoro esplorativo iniziale (ast, Klara, loop manuale)
```

## Come eseguire

```bash
pip install -r requirements.txt

# 1. scaricare ULT_Lite.jsonl in benchmark/dataset/
# 2. impostare la chiave API (mai scriverla nei file!)
#    PowerShell:  $env:NVIDIA_API_KEY = "nvapi-..."

# 3. generare i test: modello + indice del campione
python benchmark/genera.py 1b 0
```
