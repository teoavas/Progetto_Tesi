# Generazione in locale con Ollama

I tre modelli dello studio eseguiti sul proprio computer, senza dipendere da
servizi esterni. I pesi sono gli stessi rilasciati da Meta e serviti da NVIDIA;
in locale sono quantizzati a 4 bit — differenza da dichiarare in tesi.

| sigla | modello Ollama | corrispondente su NVIDIA |
|---|---|---|
| `1b` | `llama3.2:1b` | `meta/llama-3.2-1b-instruct` |
| `3b` | `llama3.2:3b` | `meta/llama-3.2-3b-instruct` |
| `8b` | `llama3.1:8b` | `meta/llama-3.1-8b-instruct` |

## Preparazione (una volta sola)

1. Installare Ollama da https://ollama.com/download (dopo l'installazione resta
   attivo in background).
2. Scaricare i modelli:

```bash
ollama pull llama3.2:1b     # ~1,3 GB
ollama pull llama3.2:3b     # ~2 GB
ollama pull llama3.1:8b     # ~4,7 GB
```

## Uso

```bash
python genera.py 1b 0            # un campione
python genera_tutti.py 1b 0 99   # i primi 100 campioni (riprende se interrotto)
python misura.py 1b              # esito e coverage dei test generati
```

I test finiscono in `generati/<modello>/test_<indice>_<funzione>.py`, le misure
in `misure_<modello>.csv`. Il dataset viene letto da `../benchmark/dataset/`:
è lo stesso per entrambe le vie, così i campioni coincidono.

Parametri identici alla versione NVIDIA: temperatura 0, `max_tokens` 1024, una
funzione per richiesta, stesso template di prompt.
