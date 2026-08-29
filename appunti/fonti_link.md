# Fonti: chiave BibTeX, riferimento e collegamento

Per ogni voce: la chiave da usare in `\cite{}`, il riferimento completo e il collegamento alla pagina ufficiale da cui verificare i dati.

**Provenienza dei dati** — è utile che tu lo sappia mentre controlli. Nelle tabelle trovi il simbolo corrispondente accanto alla chiave:

- 📄 **letto dal PDF**: `huang2025ult`, `wang2025testeval`, `schaefer2024testpilot`, `jain2025testgeneval`, `tony2025prompt`. Autori, sede e pagine vengono dal documento stesso: affidabili.
- 🔎 **confermato con ricerca sul web**: `lukasczyk2022pynguin`, `watson2020atlas`, `dinella2022toga`, `lemieux2023codamosa`, `pizzorno2024coverup`, `inozemtseva2014coverage`.
- ⚠️ **riportato dalla mia conoscenza**: `chen2021humaneval`, `austin2021mbpp`, `lozhkov2024stackv2`, `fraser2011evosuite`, `king1976symbolic`, `demoura2008z3`, `mccabe1976complexity`, `just2014mutants`, `papadakis2019mutation`, `vandeursen2001testsmells`, `llama3herd`. Sono lavori classici e i dati sono quelli standard, ma **è la categoria da verificare per prima**.
- 🔧 **strumenti software**: `pytest`, `coveragepy`, `ollama`. Il collegamento è il sito ufficiale.

Dove non sono certo dell'indirizzo esatto della pagina, trovi scritto *(da confermare)* e un collegamento di ricerca che ti porta alla scheda in pochi secondi.

---

## A. Benchmark e dataset

| chiave | riferimento | collegamento |
|---|---|---|
| 📄 `huang2025ult` | Huang, Zhang, Harman, Zhang, Du, Ng — *Benchmarking LLMs for Unit Test Generation from Real-World Functions*, 2025 | https://arxiv.org/abs/2508.00408 — versione ACM (quella linkata dalla relatrice): https://dl.acm.org/doi/10.1145/3805043 |
| 📄 `wang2025testeval` | Wang, Yang, Wang, Huang, Chu, Song, Zhang, Chen, Ma — *TestEval*, Findings of NAACL 2025, pp. 3547–3562 | https://aclanthology.org/2025.findings-naacl.197/ |
| 📄 `jain2025testgeneval` | Jain, Synnaeve, Rozière — *TestGenEval*, ICLR 2025 | https://openreview.net/forum?id=7o6SG5gVev |
| ⚠️ `chen2021humaneval` | Chen et al. — *Evaluating Large Language Models Trained on Code*, 2021 | https://arxiv.org/abs/2107.03374 |
| ⚠️ `austin2021mbpp` | Austin et al. — *Program Synthesis with Large Language Models*, 2021 | https://arxiv.org/abs/2108.07732 |
| ⚠️ `lozhkov2024stackv2` | Lozhkov et al. — *StarCoder 2 and The Stack v2*, 2024 | https://arxiv.org/abs/2402.19173 |

## B. Generazione automatica prima degli LLM

| chiave | riferimento | collegamento |
|---|---|---|
| ⚠️ `fraser2011evosuite` | Fraser, Arcuri — *EvoSuite: Automatic Test Suite Generation for Object-Oriented Software*, ESEC/FSE 2011 | https://dl.acm.org/doi/10.1145/2025113.2025179 *(da confermare)* — ricerca: https://scholar.google.com/scholar?q=EvoSuite+automatic+test+suite+generation+object-oriented+software |
| 🔎 `lukasczyk2022pynguin` | Lukasczyk, Fraser — *Pynguin: Automated Unit Test Generation for Python*, ICSE 2022 | https://arxiv.org/abs/2202.05218 — versione ACM: https://dl.acm.org/doi/10.1145/3510454.3516829 |
| ⚠️ `king1976symbolic` | King — *Symbolic Execution and Program Testing*, CACM 19(7), 1976 | https://dl.acm.org/doi/10.1145/360248.360252 *(da confermare)* |
| ⚠️ `demoura2008z3` | de Moura, Bjørner — *Z3: An Efficient SMT Solver*, TACAS 2008 | https://link.springer.com/chapter/10.1007/978-3-540-78800-3_24 *(da confermare)* |
| ⚠️ `mccabe1976complexity` | McCabe — *A Complexity Measure*, IEEE TSE SE-2(4), 1976 | https://ieeexplore.ieee.org/document/1702388 *(da confermare)* — ricerca: https://scholar.google.com/scholar?q=McCabe+A+Complexity+Measure+1976 |

## C. Generazione di assert e oracoli

| chiave | riferimento | collegamento |
|---|---|---|
| 🔎 `watson2020atlas` | Watson, Tufano, Moran, Bavota, Poshyvanyk — *On Learning Meaningful Assert Statements for Unit Test Cases*, ICSE 2020 | https://arxiv.org/abs/2002.05800 — PDF: https://www.cs.wm.edu/~denys/pubs/Learning-Asserts-ICSE'20-CRC.pdf |
| 🔎 `dinella2022toga` | Dinella, Ryan, Mytkowicz, Lahiri — *TOGA: A Neural Method for Test Oracle Generation*, ICSE 2022 | https://arxiv.org/abs/2109.09262 — versione ACM: https://dl.acm.org/doi/abs/10.1145/3510003.3510141 |

## D. Generazione di test con LLM

| chiave | riferimento | collegamento |
|---|---|---|
| 📄 `schaefer2024testpilot` | Schäfer, Nadi, Eghbali, Tip — *An Empirical Evaluation of Using LLMs for Automated Unit Test Generation*, IEEE TSE 50(1), 2024, pp. 85–105 | https://doi.org/10.1109/TSE.2023.3334955 — **verificato dalla prima pagina del PDF** in `paper/TestPilot_Schaefer_TSE2024.pdf` (volume, numero, pagine e DOI). Preprint con abstract ed export BibTeX: https://arxiv.org/abs/2302.06527 — Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2302.06527 |
| 🔎 `lemieux2023codamosa` | Lemieux, Inala, Lahiri, Sen — *CodaMOSA*, ICSE 2023 | https://www.microsoft.com/en-us/research/publication/codamosa-escaping-coverage-plateaus-in-test-generation-with-pre-trained-large-language-models/ |
| 🔎 `pizzorno2024coverup` | Altmayer Pizzorno, Berger — *CoverUp: Effective High Coverage Test Generation for Python*, 2024 | https://arxiv.org/abs/2403.16218 |

## E. Metriche e loro limiti

| chiave | riferimento | collegamento |
|---|---|---|
| 🔎 `inozemtseva2014coverage` | Inozemtseva, Holmes — *Coverage Is Not Strongly Correlated with Test Suite Effectiveness*, ICSE 2014 | https://dl.acm.org/doi/10.1145/2568225.2568271 — PDF: https://www.cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf |
| ⚠️ `just2014mutants` | Just, Jalali, Inozemtseva, Ernst, Holmes, Fraser — *Are Mutants a Valid Substitute for Real Faults in Software Testing?*, FSE 2014 | https://dl.acm.org/doi/10.1145/2635868.2635929 *(da confermare)* — ricerca: https://scholar.google.com/scholar?q=Are+mutants+a+valid+substitute+for+real+faults+in+software+testing |
| ⚠️ `papadakis2019mutation` | Papadakis, Kintis, Zhang, Jia, Le Traon, Harman — *Mutation Testing Advances: An Analysis and Survey*, Advances in Computers vol. 112, 2019 | https://www.sciencedirect.com/science/article/pii/S0065245818300305 *(da confermare)* — ricerca: https://scholar.google.com/scholar?q=Mutation+Testing+Advances+An+Analysis+and+Survey |
| 🔎 `vandeursen2001testsmells` | van Deursen, Moonen, van den Bergh, Kok — *Refactoring Test Code*, XP2001, Cagliari, 20–23 maggio 2001 | https://ir.cwi.nl/pub/4324 — PDF: https://ir.cwi.nl/pub/4324/04324D.pdf (rapporto tecnico CWI SEN-R0119). **Tutto verificato dal PDF, pagine comprese: la versione a stampa di XP2001 è di 4 pagine numerate 92–95.** Attenzione: il catalogo contiene 11 smell (Mystery Guest, Resource Optimism, Test Run War, General Fixture, Eager Test, Lazy Test, Assertion Roulette, Indirect Testing, For Testers Only, Sensitive Equality, Test Code Duplication). **Magic Number Test NON c'è**: viene da Meszaros, *xUnit Test Patterns*, 2007. |

## F. Modelli e strumenti

| chiave | riferimento | collegamento |
|---|---|---|
| ⚠️ `llama3herd` | Llama Team, AI @ Meta — *The Llama 3 Herd of Models*, 2024 | https://arxiv.org/abs/2407.21783 |
| 🔧 `pytest` | Krekel et al. — *pytest* | https://docs.pytest.org |
| 🔧 `coveragepy` | Batchelder — *coverage.py* | https://coverage.readthedocs.io |
| 🔧 `ollama` | *Ollama* | https://ollama.com |
| 📄 `tony2025prompt` | Tony, **Pintor**, Kretschmann, Scandariato — *Discrete Prompt Optimization Using Genetic Algorithm for Secure Python Code Generation*, JSS 2025 | https://www.sciencedirect.com/science/article/pii/S0164121225003516 — PDF: https://iris.unica.it/retrieve/821ed2f9-53c0-4a96-8674-68e03edc1a1f/1-s2.0-S0164121225003516-main_2.pdf |

---

## Scorciatoia per correggere una voce

Su ognuna di queste pagine c'è un pulsante per esportare la citazione già pronta:

- **arXiv**: in basso a destra, "Export BibTeX citation"
- **ACM Digital Library**: pulsante "Cite this" → scheda BibTeX
- **IEEE Xplore**: "Cite This" → BibTeX
- **ACL Anthology**: link "bib" sotto il titolo
- **Google Scholar**: le virgolette sotto il risultato → "BibTeX"

Copi quello che esce e sostituisci la voce corrispondente in `references.bib`: è il modo più rapido e non lascia errori.
