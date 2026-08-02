# Piano di lavoro — 2→20 agosto 2026

## Da portare all'appuntamento del 4 agosto

Cose fatte: setup progetto, esperimenti con `ast` e Klara, ciclo pytest+coverage funzionante, appunti scritti (`appunti/appunti_esperimenti.md`).

Domande per la professoressa:

1. Accesso API a un LLM (crediti universitari? quale modello?)
2. Benchmark di valutazione: riusare quelli del paper?
3. Metriche: statement o branch coverage? mutation testing?
4. Klara ha limiti forti con Python moderno: tenerla o puntare solo su AST+feedback?
5. Bozza struttura tesi su Overleaf (l'aveva promessa lei) e accesso al progetto Overleaf condiviso

## Roadmap 5→20 agosto (lavoro autonomo)

**5–7 ago — Prototipo fase 1 (contesto).** Script che, dato un file Python, produce il prompt per l'LLM in tre varianti: file intero, riassunto AST, file + scheletro Klara. Provarlo manualmente (anche via chat, senza API).

**8–10 ago — Prototipo fase 2 (loop di esecuzione).** Script che prende i test generati, li esegue con pytest, cattura errori/failure e costruisce il messaggio di feedback per l'iterazione successiva.

**11–13 ago — Prototipo fase 3 (feedback coverage).** Integrare `coverage`: estrarre le righe mancanti dal report, mapparle alle funzioni tramite AST, generare la richiesta di test mirati.

**14–16 ago — Integrazione.** Collegare le tre fasi in un'unica pipeline; appena disponibile la API key, sostituire il passaggio manuale con chiamate reali.

**17–19 ago — Prime misure + scrittura.** Eseguire la pipeline su un piccolo benchmark, raccogliere numeri di coverage per configurazione, aggiornare Overleaf con metodo e risultati preliminari.

**20 ago — Riepilogo per la professoressa.** Documento breve: cosa funziona, numeri ottenuti, decisioni da prendere.

Regola pratica: ogni giorno che si prova qualcosa, due righe negli appunti — è testo già pronto per la tesi.

## Struttura del progetto

```
tesi/
├── PIANO_DI_LAVORO.md          ← questo file
├── appunti/
│   └── appunti_esperimenti.md  ← note pronte per Overleaf
└── esperimenti/
    ├── funzioni_esempio.py     ← funzioni di test (3 livelli di difficoltà)
    ├── 01_ast/prova_ast.py     ← analisi AST → riassunto strutturale
    └── 02_klara/               ← scheletri di test via Z3 + coverage 100%
```

Dipendenze: `pip install klara coverage pytest`
