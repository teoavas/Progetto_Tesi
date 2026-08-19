# Bibliografia per lo stato dell'arte

24 riferimenti, tutti con dati editoriali verificabili (conferenza o rivista, anno, autori). La chiave in grassetto è quella da usare con `\cite{}`. In Overleaf usa `references.bib` con `\cite{chiave}`: i numeri li assegna LaTeX in ordine di apparizione.

★ = PDF già in `paper/`.

---

## A. Benchmark e dataset

**`huang2025ult`** ★ D. Huang, J. M. Zhang, M. Harman, Q. Zhang, M. Du, S.-K. Ng, *Benchmarking LLMs for Unit Test Generation from Real-World Functions*, arXiv:2508.00408, 2025.
→ **Fonte primaria**: definisce ULT e PLT, il dataset usato in questo lavoro. Per: decontaminazione, soglia di complessità ciclomatica, metriche Pass@k / LCov@k / BCov@k / Mut@k, risultati di riferimento.

**`wang2025testeval`** ★ W. Wang, C. Yang, Z. Wang, Y. Huang, Z. Chu, D. Song, L. Zhang, A. R. Chen, L. Ma, *TestEval: Benchmarking Large Language Models for Test Case Generation*, Findings of NAACL 2025, pp. 3547–3562.
→ Per: confronto fra benchmark, tre compiti di copertura, divario di difficoltà rispetto a ULT.

**`jain2025testgeneval`** K. Jain, G. Synnaeve, B. Rozière, *TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark*, ICLR 2025.
→ Per: mutation score come metrica; i modelli faticano a ragionare sull'esecuzione.

**`chen2021humaneval`** M. Chen et al., *Evaluating Large Language Models Trained on Code*, arXiv:2107.03374, 2021.
→ Origine di **pass@k** e di HumanEval. Da citare quando introduci la metrica.

**`austin2021mbpp`** J. Austin et al., *Program Synthesis with Large Language Models*, arXiv:2108.07732, 2021.
→ MBPP: origine dello schema di dati (`func_name`, `code`, `test_list`) che ULT eredita — spiega perché quel campo non è ground truth.

**`lozhkov2024stackv2`** A. Lozhkov et al., *StarCoder 2 and The Stack v2*, arXiv:2402.19173, 2024.
→ Il corpus da cui ULT estrae le funzioni.

## B. Generazione automatica prima degli LLM

**`fraser2011evosuite`** G. Fraser, A. Arcuri, *EvoSuite: Automatic Test Suite Generation for Object-Oriented Software*, ESEC/FSE 2011.

**`lukasczyk2022pynguin`** S. Lukasczyk, G. Fraser, *Pynguin: Automated Unit Test Generation for Python*, ICSE 2022 (Companion), pp. 168–172.
→ L'equivalente di EvoSuite per Python.

**`king1976symbolic`** J. C. King, *Symbolic Execution and Program Testing*, Communications of the ACM, 19(7), 1976, pp. 385–394.

**`demoura2008z3`** L. de Moura, N. Bjørner, *Z3: An Efficient SMT Solver*, TACAS 2008, pp. 337–340.
→ Il solver dietro Klara, nelle prove preliminari.

**`mccabe1976complexity`** T. J. McCabe, *A Complexity Measure*, IEEE TSE, SE-2(4), 1976, pp. 308–320.
→ Complessità ciclomatica: criterio di selezione di ULT.

## C. Generazione di assert e oracoli

**`watson2020atlas`** C. Watson, M. Tufano, K. Moran, G. Bavota, D. Poshyvanyk, *On Learning Meaningful Assert Statements for Unit Test Cases*, ICSE 2020, pp. 1398–1409.
→ Introduce il problema dell'**oracolo**.

**`dinella2022toga`** E. Dinella, G. Ryan, T. Mytkowicz, S. K. Lahiri, *TOGA: A Neural Method for Test Oracle Generation*, ICSE 2022, pp. 2130–2141.

## D. Generazione di test con LLM

**`schaefer2024testpilot`** ★ M. Schäfer, S. Nadi, A. Eghbali, F. Tip, *An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation*, IEEE TSE 50(1), 2024, pp. 85–105.
→ Per: costruzione del prompt, ciclo di riparazione, metrica delle **assert non banali**.

**`lemieux2023codamosa`** C. Lemieux, J. P. Inala, S. K. Lahiri, S. Sen, *CodaMOSA: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models*, ICSE 2023.
→ Approccio ibrido ricerca + LLM, costruito su Pynguin (quindi Python).

**`pizzorno2024coverup`** J. Altmayer Pizzorno, E. D. Berger, *CoverUp: Effective High Coverage Test Generation for Python*, arXiv:2403.16218, 2024.
→ Generazione guidata dalle righe non coperte: l'analogo automatico del ciclo che hai provato a mano.

## E. Metriche e loro limiti

**`inozemtseva2014coverage`** L. Inozemtseva, R. Holmes, *Coverage Is Not Strongly Correlated with Test Suite Effectiveness*, ICSE 2014, pp. 435–445.
→ **Il riferimento chiave**: giustifica l'intera tesi.

**`just2014mutants`** R. Just, D. Jalali, L. Inozemtseva, M. D. Ernst, R. Holmes, G. Fraser, *Are Mutants a Valid Substitute for Real Faults in Software Testing?*, FSE 2014, pp. 654–665.

**`papadakis2019mutation`** M. Papadakis, M. Kintis, J. Zhang, Y. Jia, Y. Le Traon, M. Harman, *Mutation Testing Advances: An Analysis and Survey*, Advances in Computers, vol. 112, 2019, pp. 275–378.

**`vandeursen2001testsmells`** A. van Deursen, L. Moonen, A. van den Bergh, G. Kok, *Refactoring Test Code*, XP 2001, pp. 92–95.
→ Introduce i **test smell** e il catalogo originario.

## F. Modelli e strumenti

**`llama3herd`** Llama Team, AI @ Meta, *The Llama 3 Herd of Models*, arXiv:2407.21783, 2024.
→ I modelli che usi vanno citati.

**`pytest`** H. Krekel et al., *pytest*, https://docs.pytest.org

**`coveragepy`** N. Batchelder, *coverage.py*, https://coverage.readthedocs.io

**`ollama`** *Ollama*, https://ollama.com

---

## Opzionali — da aggiungere solo se sviluppi quelle sezioni

Non li ho messi in `references.bib` perché sono lavori recenti su arXiv di cui non ho verificato l'elenco completo degli autori: se decidi di citarli, l'identificativo qui sotto ti porta alla scheda in trenta secondi.

| tema | riferimento | quando serve |
|---|---|---|
| test smell nei test generati da LLM | arXiv:2410.10628 (TOSEM 2025) | se sviluppi la sezione 2.5.5 con dati quantitativi (prevalenza di *Assertion Roulette* e *Magic Number Test*) |
| copertura e mutation score sulle suite da LLM | arXiv:2607.22880 | se vuoi legare il classico del 2014 direttamente agli LLM |
| rassegna sulla generazione di unit test con LLM | arXiv:2511.21382 | per la chiusura del capitolo |
| generazione iterativa con riparazione | TestART, arXiv:2408.03095 | solo se parli di approcci iterativi |
| benchmark su modifiche di repository | SWT-Bench, arXiv:2406.12952 | solo se allarghi la tabella dei benchmark |
| mutation testing per Python | Cosmic Ray, github.com/sixty-north/cosmic-ray | se usi davvero il mutation score |

---

## Note pratiche

- Ventiquattro riferimenti sono adeguati per una triennale. Meglio quindici citati davvero nel testo che trenta elencati.
- Ogni affermazione contestabile deve avere una fonte a fine frase.
- I dati qui riportati sono quelli standard: una verifica veloce su Google Scholar prima della consegna resta buona prassi, ma non dovrebbe riservare sorprese.
