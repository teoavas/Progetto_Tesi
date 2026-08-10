# Progetto tesi — Valutazione della generazione di unit test con LLM

Tesi triennale di Matteo Savastano — Università degli Studi di Cagliari.

## Obiettivo

Misurare la qualità degli unit test generati da modelli linguistici di piccola taglia (Llama 1B, 3B, 8B) su funzioni Python reali, a parità di prompt e con temperatura 0.

Metriche previste:

- **coverage** del codice sotto test
- **ripetizione delle righe**: quante volte ogni riga viene rieseguita
- **duplicazione** tra i file di test generati
- **esito**: test passato / eseguibile ma fallito / non eseguibile

Dataset: [UnLeakedTestBench](https://github.com/huangd1999/UnLeakedTestBench) (`ULT_Lite.jsonl`, 200 campioni; se ne usano i primi 100).

## Struttura

```
benchmark/
├── dataset/ULT_Lite.jsonl   dataset (un campione JSON per riga)
├── chiave.py                chiave API (ignorato da git)
├── genera.py                genera i test per un campione con un modello
├── genera_tutti.py          ciclo su piu' campioni, salta quelli gia' fatti
├── generati/<modello>/      i test prodotti, un file per campione
└── generazioni.csv          registro: finish_reason, tentativi, secondi

appunti/                     note di lavoro (bozza per la tesi)
preliminare/                 lavoro esplorativo iniziale (ast, Klara, loop manuale)
```

## Come eseguire

```bash
pip install -r requirements.txt

# la chiave API va messa in benchmark/chiave.py (mai versionata)

python benchmark/genera.py 8b 0            # un campione
python benchmark/genera_tutti.py 8b 0 99   # i primi 100 campioni
```

Modelli disponibili: `1b`, `3b`, `8b` (oggetto dello studio) e `70b` (solo come controllo).

## Parametri congelati

Temperatura 0, `max_tokens` 1024, un prompt fisso con sezioni `[instruction]` / `[data]` / `[format]`, una funzione per richiesta. Cambiarli richiede di rigenerare tutti i campioni.
