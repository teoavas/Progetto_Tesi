# Bibliografia per lo stato dell'arte

Riferimenti numerati e raggruppati per tema. Il numero fra parentesi quadre è quello usato nella struttura del capitolo (`stato_dell_arte.md`). In Overleaf conviene usare `references.bib` (stessa cartella) con `\cite{chiave}`: i numeri li assegna LaTeX da solo, in ordine di apparizione.

I PDF contrassegnati con ★ sono già in `paper/`.

---

## A. Il dataset e i benchmark di riferimento

**[1]** ★ D. Huang, J. M. Zhang, M. Harman, Q. Zhang, M. Du, S.-K. Ng, *Benchmarking LLMs for Unit Test Generation from Real-World Functions*, arXiv:2508.00408, 2025.
→ Fonte primaria: definisce UnLeakedTestBench (ULT) e PreLeakedTestBench (PLT), il dataset da cui provengono le funzioni usate in questo lavoro. Da citare per: decontaminazione, complessità ciclomatica ≥ 10, metriche Pass@k / LCov@k / BCov@k / Mut@k, risultati di riferimento (41,32% Pass@1 medio).

**[2]** ★ W. Wang, C. Yang, Z. Wang, Y. Huang, Z. Chu, D. Song, L. Zhang, A. R. Chen, L. Ma, *TestEval: Benchmarking Large Language Models for Test Case Generation*, Findings of NAACL 2025, pp. 3547–3562.
→ Benchmark su 210 programmi LeetCode, con tre compiti: copertura complessiva, copertura mirata di riga/ramo, copertura mirata di cammino. Da citare per: il confronto fra benchmark e il divario di difficoltà rispetto a ULT.

**[3]** K. Jain, G. Synnaeve, B. Rozière, *TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark*, ICLR 2025.
→ Benchmark a livello di file costruito su SWE-bench. Da citare per: mutation score come metrica, e per l'osservazione che i modelli faticano a ragionare sull'esecuzione (errori nelle assert sui cammini complessi).

**[4]** N. Mündler et al., *SWT-Bench: Testing and Validating Real-World Bug-Fixes with Code Agents*, NeurIPS 2024, arXiv:2406.12952.
→ Da citare nella tabella comparativa dei benchmark.

**[5]** M. Chen et al., *Evaluating Large Language Models Trained on Code*, arXiv:2107.03374, 2021.
→ Origine della metrica **pass@k** e del benchmark HumanEval. Da citare quando introduci Pass@k.

**[6]** J. Austin et al., *Program Synthesis with Large Language Models*, arXiv:2108.07732, 2021.
→ MBPP: da citare come antenato dei benchmark e come origine dello schema di dati (`func_name`, `code`, `test_list`) che ULT eredita.

**[7]** A. Lozhkov et al., *StarCoder 2 and The Stack v2*, arXiv:2402.19173, 2024.
→ The Stack v2 è il corpus da cui ULT estrae le funzioni. Da citare quando descrivi la provenienza del dataset.

---

## B. Generazione automatica di test prima degli LLM

**[8]** G. Fraser, A. Arcuri, *EvoSuite: Automatic Test Suite Generation for Object-Oriented Software*, ESEC/FSE 2011.
→ Il riferimento classico per la generazione search-based.

**[9]** S. Lukasczyk, G. Fraser, *Pynguin: Automated Unit Test Generation for Python*, ICSE 2022 (Demonstrations), arXiv:2202.05218.
→ L'equivalente di EvoSuite per Python: da citare perché il tuo lavoro è su Python.

**[10]** J. C. King, *Symbolic Execution and Program Testing*, Communications of the ACM, 19(7), 1976.
→ Il fondamento dell'esecuzione simbolica.

**[11]** L. de Moura, N. Bjørner, *Z3: An Efficient SMT Solver*, TACAS 2008.
→ Il solver usato da Klara nelle tue prove preliminari.

**[12]** T. J. McCabe, *A Complexity Measure*, IEEE Transactions on Software Engineering, SE-2(4), 1976.
→ Definizione della complessità ciclomatica: da citare quando spieghi il criterio di selezione di ULT.

---

## C. Generazione di assert e oracoli (pre-LLM)

**[13]** C. Watson, M. Tufano, K. Moran, G. Bavota, D. Poshyvanyk, *On Learning Meaningful Assert Statements for Unit Test Cases* (ATLAS), ICSE 2020, arXiv:2002.05800.
→ Primo approccio neurale alla generazione di assert. Da citare per introdurre il problema dell'**oracolo**.

**[14]** E. Dinella, G. Ryan, T. Mytkowicz, S. K. Lahiri, *TOGA: A Neural Method for Test Oracle Generation*, ICSE 2022, arXiv:2109.09262.
→ Inferenza di oracoli di assert e di eccezione; integrato con EvoSuite trova 57 difetti reali.

---

## D. Generazione di test con LLM

**[15]** ★ M. Schäfer, S. Nadi, A. Eghbali, F. Tip, *An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation* (TestPilot), IEEE Transactions on Software Engineering, 50(1), 2024, pp. 85–105.
→ Generazione senza addestramento né few-shot; 70,2% di copertura di istruzioni mediana. Da citare per: costruzione del prompt, ciclo di riparazione, e la metrica delle **assert non banali**.

**[16]** C. Lemieux, J. P. Inala, S. K. Lahiri, S. Sen, *CodaMOSA: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models*, ICSE 2023.
→ Approccio ibrido: quando la ricerca si arena, l'LLM propone casi di test per le funzioni poco coperte. Costruito su Pynguin, quindi su Python.

**[17]** J. Altmayer Pizzorno, E. D. Berger, *CoverUp: Effective High Coverage Test Generation for Python*, arXiv:2403.16218, 2024.
→ Genera test guidato dai segmenti di codice non coperti, iterando col modello quando i test falliscono. È l'analogo automatico dell'esperimento manuale che hai fatto nelle prove preliminari.

**[18]** Z. Yuan et al., *No More Manual Tests? Evaluating and Improving ChatGPT for Unit Test Generation* (ChatTester), arXiv:2305.04207, 2023.

**[19]** Y. Xie et al., *ChatUniTest: A Framework for LLM-Based Test Generation*, arXiv:2305.04764, 2023.

**[20]** S. Gu et al., *TestART: Improving LLM-based Unit Testing via Co-evolution of Automated Generation and Repair Iteration*, arXiv:2408.03095, 2024.

**[21]** J. Wang, Y. Huang, C. Chen, Z. Liu, S. Wang, Q. Wang, *Software Testing with Large Language Models: Survey, Landscape, and Vision*, IEEE Transactions on Software Engineering, 2024, arXiv:2307.07221.
→ Rassegna generale: utile per inquadrare il campo in poche righe senza citare venti lavori singoli.

**[22]** *Large Language Models for Unit Test Generation: Achievements, Challenges, and Opportunities*, arXiv:2511.21382, 2025.
→ Rassegna specifica sulla generazione di unit test: la più aggiornata, ottima per la chiusura del capitolo.

---

## E. Metriche e loro limiti *(la parte più importante per questa tesi)*

**[23]** L. Inozemtseva, R. Holmes, *Coverage Is Not Strongly Correlated with Test Suite Effectiveness*, ICSE 2014.
→ **Il riferimento chiave della tesi**: controllando la dimensione della suite, la correlazione fra copertura ed efficacia scende a bassa o moderata. È l'argomento che giustifica l'uso di metriche affiancate alla copertura.

**[24]** R. Just, D. Jalali, L. Inozemtseva, M. D. Ernst, R. Holmes, G. Fraser, *Are Mutants a Valid Substitute for Real Faults in Software Testing?*, FSE 2014.
→ Giustifica il mutation score come indicatore di capacità di rilevare difetti reali.

**[25]** M. Papadakis, M. Kintis, J. Zhang, Y. Jia, Y. Le Traon, M. Harman, *Mutation Testing Advances: An Analysis and Survey*, Advances in Computers, 2019.
→ Rassegna sul mutation testing, per non doverne citare dieci.

**[26]** *Do Coverage and Mutation Scores of LLM-Generated Test Suites Correlate with Their Effectiveness?* (studio di replicabilità), arXiv:2607.22880, 2026.
→ Riporta la domanda di [23] direttamente sulle suite generate da LLM: il collegamento più diretto fra il classico del 2014 e il tuo lavoro.

**[27]** A. van Deursen, L. Moonen, A. van den Bergh, G. Kok, *Refactoring Test Code*, XP 2001.
→ Il lavoro che introduce il concetto di **test smell** e ne dà il catalogo originario.

**[28]** *On the Diffusion of Test Smells in LLM-Generated Unit Tests*, ACM TOSEM, 2025, arXiv:2410.10628.
→ Analisi su larga scala dei test smell nei test generati da LLM: prevalgono *Assertion Roulette* e *Magic Number Test*. Da citare nella sezione sulla qualità del codice di test.

---

## F. Modelli e strumenti usati nel lavoro

**[29]** Llama Team, AI @ Meta, *The Llama 3 Herd of Models*, arXiv:2407.21783, 2024.
→ Vanno citati i modelli che usi: non basta scrivere "Llama 3.2 1B".

**[30]** Ollama, https://ollama.com — infrastruttura di esecuzione locale dei modelli.

**[31]** H. Krekel et al., *pytest*, https://docs.pytest.org — esecuzione dei test.

**[32]** N. Batchelder, *coverage.py*, https://coverage.readthedocs.io — misura della copertura.

**[33]** *Cosmic Ray: mutation testing for Python*, https://github.com/sixty-north/cosmic-ray — strumento di mutation testing usato da ULT.

---

## Note pratiche

- **Prima della consegna**, verifica pagine, DOI e nomi degli autori su Google Scholar o sulla pagina ufficiale della conferenza: qui sono riportati i dati essenziali, ma i dettagli editoriali vanno confermati.
- **Quantità**: 33 riferimenti sono adeguati per uno stato dell'arte di una tesi triennale. Non serve citarli tutti: meglio 20 usati davvero nel testo che 33 elencati e mai richiamati.
- **Regola pratica**: ogni affermazione che un lettore potrebbe contestare ("gli strumenti tradizionali producono test poco leggibili") deve avere una fonte a fine frase.
- I riferimenti in `references.bib` hanno chiavi parlanti (`huang2025ult`, `inozemtseva2014coverage`, …) da usare con `\cite{}`.
