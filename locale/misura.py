"""Parte dinamica: esegue i test generati e ne misura esito, copertura e duplicazione.

Per ogni file generato:
  1. controllo sintattico con ast.parse   -> se fallisce: "non eseguibile"
  2. esecuzione con pytest in una cartella isolata e con limite di tempo
  3. copertura di riga e di ramo sulla sola funzione sotto test, calcolata due
     volte: con tutti i test (cov_righe, cov_rami) e con i soli test che passano
     (cov_righe_ok, cov_rami_ok). La prima dice quanto codice viene *eseguito*,
     la seconda quanto ne viene davvero *verificato*: la distanza fra le due
     misura quanto la copertura sopravvaluta cio' che i test garantiscono
  4. duplicazione fra le righe di test

Esito attribuito a ciascun campione:
  non_eseguibile  errore di sintassi, import fallito, nessun test raccolto
  fallito         i test girano ma almeno uno non passa
  passato         tutti i test passano
  timeout         l'esecuzione non termina entro il limite

L'output integrale di pytest viene salvato in report/<sigla>/<indice>.txt:
serve per analizzare i fallimenti e raggrupparli per categoria.

Le misure statiche (sintassi, aderenza al formato, tempo di generazione) stanno
in statiche.csv e si uniscono a queste su (modello, indice).

Attenzione a n_test: qui e' il numero di casi eseguiti da pytest, che conta
separatamente le istanze di un test parametrizzato; in statiche.csv e' invece
il numero di funzioni di test presenti nel sorgente. I due valori possono
differire, e vanno usati per scopi diversi.

Uso:  python misura.py 8b [limite_secondi]
"""

import ast
import collections
import csv
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

QUI = Path(__file__).parent
DATASET = QUI.parent / "benchmark" / "dataset" / "ULT_Lite.jsonl"
sigla = sys.argv[1]
LIMITE_SECONDI = int(sys.argv[2]) if len(sys.argv) > 2 else 60

# Il campo "code" del dataset non include gli import di cui la funzione ha
# bisogno (re, math, ...): senza questo preambolo alcune funzioni sollevano
# NameError e i test risultano falliti per un motivo che non riguarda il
# modello. "pragma: no cover" tiene queste righe fuori dal calcolo di coverage.
PREAMBOLO = ("import re, math, os, sys, json, string, itertools, collections, "
             "functools, datetime, random, copy  # pragma: no cover\n\n")

campioni = [json.loads(r) for r in
            DATASET.read_text(encoding="utf-8").splitlines()]

REPORT = QUI / "report" / sigla
REPORT.mkdir(parents=True, exist_ok=True)

# pytest -v stampa una riga per test:  test_generato.py::test_x_1 PASSED  [ 12%]
ESITO_TEST = re.compile(r"::(\S+)\s+(PASSED|FAILED|ERROR)")


def duplicazione(righe):
    """Percentuale di righe ripetute sul totale delle righe di test.

    Si ignorano righe vuote e commenti. Una riga presente n volte contribuisce
    n-1 ripetizioni: il risultato e' la quota di codice ridondante.
    """
    utili = [r.strip() for r in righe
             if r.strip() and not r.strip().startswith("#")]
    if not utili:
        return 0.0
    conteggio = collections.Counter(utili)
    ripetute = sum(n - 1 for n in conteggio.values() if n > 1)
    return round(100 * ripetute / len(utili), 1)


def righe_dei_test(sorgente, nomi):
    """Righe appartenenti alle funzioni di test elencate in `nomi`.

    pytest riporta i test parametrizzati come voci distinte (test_x[1],
    test_x[2], ...): il suffisso fra parentesi va tolto per ritrovare la
    funzione nell'albero sintattico.
    """
    nomi = {n.split("[")[0] for n in nomi}
    linee = sorgente.splitlines()
    fuori = []
    for nodo in ast.parse(sorgente).body:
        if isinstance(nodo, ast.FunctionDef) and nodo.name in nomi:
            fuori.extend(linee[nodo.lineno - 1:nodo.end_lineno])
    return fuori


def misura(percorso_test, codice_funzione, indice):
    """Esegue un file di test in isolamento. Restituisce un dizionario di misure."""
    vuoto = {"esito": "non_eseguibile", "n_test": 0, "passati": 0, "falliti": 0,
             "errori": 0, "cov_righe": 0.0, "cov_rami": 0.0,
             "cov_righe_ok": 0.0, "cov_rami_ok": 0.0,
             "dup_tutti": 0.0, "dup_passati": 0.0}
    sorgente = percorso_test.read_text(encoding="utf-8")
    try:
        ast.parse(sorgente)
    except SyntaxError:
        return vuoto

    lavoro = Path(tempfile.mkdtemp())
    try:
        (lavoro / "funzione.py").write_text(
            PREAMBOLO + codice_funzione.strip() + "\n", encoding="utf-8")
        (lavoro / "test_generato.py").write_text(sorgente, encoding="utf-8")

        comando = [sys.executable, "-m", "coverage", "run", "--branch",
                   "--source=funzione", "-m", "pytest", "test_generato.py",
                   "-v", "--tb=short", "-p", "no:cacheprovider"]
        try:
            esecuzione = subprocess.run(comando, cwd=lavoro, capture_output=True,
                                        text=True, timeout=LIMITE_SECONDI)
        except subprocess.TimeoutExpired:
            (REPORT / f"{indice:03d}.txt").write_text(
                "TIMEOUT\n", encoding="utf-8")
            return {**vuoto, "esito": "timeout"}

        uscita = esecuzione.stdout + esecuzione.stderr
        # Report integrale: e' la base per la categorizzazione dei fallimenti.
        (REPORT / f"{indice:03d}.txt").write_text(uscita, encoding="utf-8")

        esiti = dict(ESITO_TEST.findall(uscita))
        passati = [n for n, e in esiti.items() if e == "PASSED"]
        falliti = [n for n, e in esiti.items() if e == "FAILED"]
        errori = [n for n, e in esiti.items() if e == "ERROR"]

        if esecuzione.returncode == 0 and passati:
            stato = "passato"
        elif not passati and not falliti:
            stato = "non_eseguibile"   # import fallito o nessun test raccolto
        elif errori and not falliti:
            stato = "non_eseguibile"
        else:
            stato = "fallito"

        def copertura(nome_file):
            """Legge il report json prodotto da coverage e ne ricava le due misure."""
            subprocess.run([sys.executable, "-m", "coverage", "json",
                            "-o", nome_file, "-q"],
                           cwd=lavoro, capture_output=True, text=True)
            f = lavoro / nome_file
            if not f.exists():
                return 0.0, 0.0
            t = json.loads(f.read_text(encoding="utf-8"))["totals"]
            righe = 100 * t["covered_lines"] / t["num_statements"] if t["num_statements"] else 0.0
            rami = 100 * t["covered_branches"] / t["num_branches"] if t.get("num_branches") else 0.0
            return righe, rami

        cov_righe = cov_rami = 0.0
        cov_righe_ok = cov_rami_ok = 0.0
        if stato in ("passato", "fallito"):
            cov_righe, cov_rami = copertura("cov.json")

            # Seconda esecuzione con i soli test che passano: misura quanto
            # codice viene davvero *verificato*, non solo eseguito. La prima
            # copertura conta anche i test che falliscono, perche' un assert
            # sbagliato esegue comunque la funzione prima di sollevare l'errore.
            if passati and falliti:
                (lavoro / ".coverage").unlink(missing_ok=True)
                soli_passati = [f"test_generato.py::{n}" for n in passati]
                try:
                    subprocess.run(
                        [sys.executable, "-m", "coverage", "run", "--branch",
                         "--source=funzione", "-m", "pytest", *soli_passati,
                         "-q", "--no-header", "-p", "no:cacheprovider"],
                        cwd=lavoro, capture_output=True, text=True,
                        timeout=LIMITE_SECONDI)
                    cov_righe_ok, cov_rami_ok = copertura("cov_ok.json")
                except subprocess.TimeoutExpired:
                    pass
            elif passati:      # passano tutti: coincide con la prima misura
                cov_righe_ok, cov_rami_ok = cov_righe, cov_rami

        return {"esito": stato, "n_test": len(esiti),
                "passati": len(passati), "falliti": len(falliti),
                "errori": len(errori),
                "cov_righe": round(cov_righe, 1), "cov_rami": round(cov_rami, 1),
                "cov_righe_ok": round(cov_righe_ok, 1),
                "cov_rami_ok": round(cov_rami_ok, 1),
                # due basi: tutti i test, oppure i soli test che passano.
                # Quale riportare dipende da come si definisce "successo".
                "dup_tutti": duplicazione(sorgente.splitlines()),
                "dup_passati": duplicazione(righe_dei_test(sorgente, set(passati)))}
    finally:
        shutil.rmtree(lavoro, ignore_errors=True)


COLONNE = ["modello", "indice", "func_name", "esito", "n_test", "passati",
           "falliti", "errori", "cov_righe", "cov_rami", "cov_righe_ok", "cov_rami_ok",
           "dup_tutti", "dup_passati"]
uscita = QUI / f"misure_{sigla}.csv"

# salva riga per riga e salta cio' che e' gia' stato misurato:
# si puo' interrompere e riprendere
gia_fatti = set()
if uscita.exists():
    gia_fatti = {int(r["indice"]) for r in csv.DictReader(uscita.open(encoding="utf-8"))}

nuovo = not uscita.exists()
with uscita.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLONNE)
    if nuovo:
        w.writeheader()
    for percorso in sorted((QUI / "generati" / sigla).glob("test_*.py")):
        indice = int(percorso.name.split("_")[1])
        if indice in gia_fatti:
            continue
        campione = campioni[indice]
        m = misura(percorso, campione["code"], indice)
        w.writerow({"modello": sigla, "indice": indice,
                    "func_name": campione["func_name"], **m})
        f.flush()
        print(f"[{indice:>3}] {campione['func_name'][:30]:<30} {m['esito']:<15} "
              f"{m['passati']}p/{m['falliti']}f  righe {m['cov_righe']}%  "
              f"rami {m['cov_rami']}%  dup {m['dup_tutti']}%", flush=True)

print(f"\n-> {uscita.name}  e report/{sigla}/")
