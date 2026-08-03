# Piano di lavoro — 2→20 agosto 2026

## Da portare all'appuntamento del 4 agosto

Cose fatte: setup progetto, esperimenti con `ast` e Klara, ciclo pytest+coverage funzionante, repo su GitHub con CI (test automatici a ogni push), simulazione manuale del loop con LLM via chat in due round — funzioni semplici (47% → 100% con una iterazione di feedback) e funzioni complesse (98% al primo giro, con scoperta di una riga irraggiungibile: vedi esperimento 5 negli appunti). Avviata la cartella `esperimenti/03_ciclo/` per il prototipo dello script di orchestrazione (`ciclo.py`, da completare).

Domande per la professoressa:

1. Accesso API a un LLM (crediti universitari? quale modello?)
2. Benchmark di valutazione: riusare quelli del paper (es. TestGenEval-Lite, 160 coppie)? Su funzioni semplici la coverage è perfetta comunque: serve codice dove il primo tentativo fallisce
3. Metriche: statement o branch coverage? mutation testing?
4. Klara ha limiti forti con Python moderno (non si installa su Python 3.12): tenerla o puntare solo su AST+feedback?
5. Bozza struttura tesi su Overleaf (l'aveva promessa lei) e accesso al progetto Overleaf condiviso
6. Criterio di stop del loop: plateau di coverage o N iterazioni? Le righe che restano scoperte vanno segnalate come possibile codice morto?

## Roadmap 5→20 agosto (lavoro autonomo)

**5–7 ago — Completare `ciclo.py` (semi-automatico).** Lo script che orchestra il loop: genera il prompt (con feedback di errori o righe scoperte a seconda dello stato), esegue pytest+coverage, estrae le righe mancanti dal report. Il passaggio verso l'LLM resta manuale (copia-incolla in chat) finché non c'è la API. In parte già impostato in `esperimenti/03_ciclo/`.

**8–10 ago — Prototipo fase 1 (varianti di contesto).** Estendere la generazione del prompt in tre varianti da confrontare: file intero, riassunto AST, file + scheletro Klara. Provarle manualmente sullo stesso bersaglio e annotare le differenze.

**11–13 ago — Integrazione API (se disponibile dopo l'incontro).** Sostituire il copia-incolla manuale con la chiamata al modello; aggiungere il criterio di stop (plateau di coverage / N iterazioni max).

**14–16 ago — Integrazione.** Collegare le tre fasi in un'unica pipeline; appena disponibile la API key, sostituire il passaggio manuale con chiamate reali.

**17–19 ago — Prime misure + scrittura.** Eseguire la pipeline su un piccolo benchmark, raccogliere numeri di coverage per configurazione, aggiornare Overleaf con metodo e risultati preliminari.

**20 ago — Riepilogo per la professoressa.** Documento breve: cosa funziona, numeri ottenuti, decisioni da prendere.

Regola pratica: ogni giorno che si prova qualcosa, due righe negli appunti — è testo già pronto per la tesi.

## Struttura del progetto

```
tesi/
├── README.md                   ← presentazione del repo (visibile su GitHub)
├── PIANO_DI_LAVORO.md          ← questo file
├── appunti/
│   └── appunti_esperimenti.md  ← note pronte per Overleaf (5 esperimenti)
└── esperimenti/
    ├── funzioni_esempio.py     ← funzioni di test (3 livelli di difficoltà)
    ├── test_llm1.py            ← test generati da LLM via chat (esperimento 4)
    ├── 01_ast/prova_ast.py     ← analisi AST → riassunto strutturale
    ├── 02_klara/               ← scheletri di test via Z3 + coverage 100%
    └── 03_ciclo/               ← prototipo del loop: bersaglio, test LLM, ciclo.py
```

Dipendenze: `pip install klara coverage pytest`
