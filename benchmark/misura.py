"""Esegue i test generati e ne misura esito e coverage.

Per ogni file generato:
  1. controllo sintattico con ast.parse   -> se fallisce: "non eseguibile"
  2. esecuzione con pytest in una cartella isolata e con timeout
  3. coverage della sola funzione sotto test

Esito attribuito a ciascun campione:
  non_eseguibile  errore di sintassi, import fallito, nessun test raccolto
  fallito         i test girano ma almeno uno non passa
  passato         tutti i test passano
  timeout         l'esecuzione non termina entro il limite

Uso:  python misura.py 8b
"""

import ast
import csv
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

QUI = Path(__file__).parent
sigla = sys.argv[1]
LIMITE_SECONDI = int(sys.argv[2]) if len(sys.argv) > 2 else 60

# Il campo "code" del dataset non include gli import di cui la funzione ha
# bisogno (re, math, ...): senza questo preambolo alcune funzioni sollevano
# NameError e i test risultano falliti per un motivo che non riguarda il
# modello. "pragma: no cover" tiene queste righe fuori dal calcolo di coverage.
PREAMBOLO = ("import re, math, os, sys, json, string, itertools, collections, "
             "functools, datetime, random, copy  # pragma: no cover\n\n")
campioni = [json.loads(r) for r in
            (QUI / "dataset" / "ULT_Lite.jsonl").read_text(encoding="utf-8").splitlines()]


def conta(testo, parola):
    m = re.search(rf"(\d+) {parola}", testo)
    return int(m.group(1)) if m else 0


def misura(percorso_test, codice_funzione):
    """Esegue un file di test in isolamento. Restituisce (esito, n_pass, n_fail, coverage)."""
    sorgente = percorso_test.read_text(encoding="utf-8")
    try:
        ast.parse(sorgente)
    except SyntaxError:
        return "non_eseguibile", 0, 0, 0.0

    lavoro = Path(tempfile.mkdtemp())
    try:
        (lavoro / "funzione.py").write_text(PREAMBOLO + codice_funzione.strip() + "\n", encoding="utf-8")
        (lavoro / "test_generato.py").write_text(sorgente, encoding="utf-8")

        comando = [sys.executable, "-m", "coverage", "run", "--source=funzione",
                   "-m", "pytest", "test_generato.py", "-q", "--no-header", "-p", "no:cacheprovider"]
        try:
            esito = subprocess.run(comando, cwd=lavoro, capture_output=True,
                                   text=True, timeout=LIMITE_SECONDI)
        except subprocess.TimeoutExpired:
            return "timeout", 0, 0, 0.0

        uscita = esito.stdout + esito.stderr
        passati, falliti = conta(uscita, "passed"), conta(uscita, "failed")
        errori = conta(uscita, "error")

        if esito.returncode == 0:
            stato = "passato"
        elif passati == 0 and falliti == 0:
            stato = "non_eseguibile"   # import fallito o nessun test raccolto
        elif errori and not falliti:
            stato = "non_eseguibile"
        else:
            stato = "fallito"

        copertura = 0.0
        if stato in ("passato", "fallito"):
            subprocess.run([sys.executable, "-m", "coverage", "json", "-o", "cov.json", "-q"],
                           cwd=lavoro, capture_output=True, text=True)
            f = lavoro / "cov.json"
            if f.exists():
                dati = json.loads(f.read_text(encoding="utf-8"))
                copertura = dati["totals"]["percent_covered"]
        return stato, passati, falliti, round(copertura, 1)
    finally:
        shutil.rmtree(lavoro, ignore_errors=True)


uscita = QUI / f"misure_{sigla}.csv"

# salva riga per riga e salta cio' che e' gia' stato misurato:
# si puo' interrompere e riprendere
gia_fatti = set()
if uscita.exists():
    gia_fatti = {int(r["indice"]) for r in csv.DictReader(uscita.open(encoding="utf-8"))}

nuovo = not uscita.exists()
with uscita.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    if nuovo:
        w.writerow(["modello", "indice", "func_name", "esito", "passati", "falliti", "coverage"])
    for percorso in sorted((QUI / "generati" / sigla).glob("test_*.py")):
        indice = int(percorso.name.split("_")[1])
        if indice in gia_fatti:
            continue
        campione = campioni[indice]
        stato, passati, falliti, copertura = misura(percorso, campione["code"])
        w.writerow([sigla, indice, campione["func_name"], stato, passati, falliti, copertura])
        f.flush()
        print(f"[{indice:>3}] {campione['func_name'][:32]:<32} {stato:<15} "
              f"{passati}p/{falliti}f  cov {copertura}%", flush=True)

print(f"\n-> {uscita.name}")
