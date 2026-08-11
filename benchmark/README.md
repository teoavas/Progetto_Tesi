# Generazione con NVIDIA build — materiale conservato

Questa cartella contiene il lavoro svolto con i modelli serviti da **NVIDIA build**,
prima del passaggio all'esecuzione in locale (vedi `../locale/`).

Il materiale è conservato perché resta valido e utilizzabile:

- `generati/8b/` — 100 test generati con `meta/llama-3.1-8b-instruct`
- `generati/70b/` — una generazione con il modello da 70B, usata come controllo
- `generazioni.csv` — registro delle 100 generazioni: `finish_reason`, tentativi, secondi
- `misure_8b.csv` — esito e coverage per ciascuno dei 100 campioni
- `genera.py`, `genera_tutti.py`, `misura.py` — gli script usati

**Perché è stato interrotto.** Gli endpoint dei tre modelli piccoli hanno mostrato
disponibilità intermittente: dopo aver funzionato regolarmente per i 100 campioni
dell'8B, hanno smesso di rispondere anche a una richiesta minima ("hi", 5 token),
su tutti e tre i modelli e sul 70B. Non è un problema del client: la stessa
configurazione aveva funzionato poco prima.

**Uso previsto.** I risultati dell'8B ottenuti qui restano disponibili come termine
di paragone fra modello a piena precisione (NVIDIA) e modello quantizzato a 4 bit
(Ollama), sullo stesso identico campione e con lo stesso prompt.

Lo script di misura `misura.py` è indipendente dal luogo di generazione e viene
riusato anche per i risultati prodotti in locale.
