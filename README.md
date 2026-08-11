# Progetto tesi — Valutazione della generazione di unit test con LLM

Tesi triennale di Matteo Savastano — Università degli Studi di Cagliari.

## Obiettivo

Misurare la qualità degli unit test generati da modelli linguistici di piccola taglia (Llama 1B, 3B, 8B) su 100 funzioni Python reali, a parità di prompt e con temperatura 0.

Metriche previste:

- **esito**: test passato / eseguibile ma fallito / non eseguibile
- **coverage** del codice sotto test
- **ripetizione delle righe**: quante volte ogni riga viene rieseguita
- **duplicazione** tra i file di test generati

Dataset: [UnLeakedTestBench](https://github.com/huangd1999/UnLeakedTestBench) (`ULT_Lite.jsonl`, 200 campioni; se ne usano i primi 100).

## Struttura

```
locale/          lavoro corrente: modelli eseguiti con Ollama sul pc
├── genera.py            genera i test per un campione
├── genera_tutti.py      ciclo sui campioni, riprende se interrotto
├── misura.py            esegue i test e misura esito e coverage
└── generati/<modello>/  i test prodotti

benchmark/       materiale conservato: generazione con NVIDIA build
├── dataset/ULT_Lite.jsonl   il dataset, condiviso da entrambe le vie
├── generati/8b/             100 test generati con llama-3.1-8b
├── generazioni.csv          registro (finish_reason, tentativi, secondi)
└── misure_8b.csv            esito e coverage dei 100 campioni

appunti/         note di lavoro (bozza per la tesi)
preliminare/     lavoro esplorativo iniziale (ast, Klara, loop manuale)
```

Perché due cartelle: la generazione è iniziata sui modelli serviti da NVIDIA build, i cui endpoint si sono poi rivelati intermittenti fino a non rispondere più. Il lavoro prosegue in locale con Ollama, dove gli stessi modelli sono sempre disponibili. Il materiale NVIDIA è conservato: resta valido e utile come confronto fra pesi a piena precisione e pesi quantizzati.

## Come eseguire

```bash
pip install -r requirements.txt
# installare Ollama da https://ollama.com/download
ollama pull llama3.2:1b

cd locale
python genera_tutti.py 1b 0 99
python misura.py 1b
```

## Parametri congelati

Temperatura 0, `max_tokens` 1024, una funzione per richiesta, prompt fisso con sezioni `[instruction]` / `[data]` / `[format]`. Cambiarli richiede di rigenerare tutti i campioni.
