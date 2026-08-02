# Progetto tesi — Generazione di unit test con LLM e feedback di coverage

Tesi triennale di Matteo Savastano.

## Idea

Partendo dal paper [TestGenEval](https://openreview.net/pdf?id=7o6SG5gVev), in cui gli LLM generano unit test senza contesto aggiuntivo, la tesi studia se la coverage migliora dando al modello:

1. **Contesto strutturale** sul codice (AST, scheletri di test generati con Klara)
2. **Feedback di esecuzione** (errori dei test, iterando fino a test funzionanti)
3. **Feedback di coverage** (le righe non coperte, per generare test mirati)

## Struttura del repository

```
├── PIANO_DI_LAVORO.md          roadmap e domande aperte
├── appunti/                    note di lavoro (bozza per la tesi su Overleaf)
└── esperimenti/
    ├── funzioni_esempio.py     funzioni di prova a difficoltà crescente
    ├── 01_ast/                 estrazione di contesto strutturale con ast
    └── 02_klara/               scheletri di test con Klara + pytest + coverage
```

## Come eseguire

```bash
pip install klara coverage pytest

# analisi AST
python esperimenti/01_ast/prova_ast.py

# generazione scheletri di test + coverage
cd esperimenti/02_klara
klara funzioni_per_klara.py
coverage run -m pytest
coverage report -m
```

A ogni push, GitHub Actions esegue automaticamente i test con coverage (vedi tab Actions).
