"""Misure statiche: tutto cio' che si stabilisce senza eseguire i test.

Per ogni campione di ogni modello:
  - stato:      non_tentato / non_scritto / scritto
  - troncamento: finish_reason preso da generazioni.csv
  - sintassi:   ast.parse, senza eseguire nulla
  - formato:    vincoli del prompt verificati sull'AST
  - tempo:      secondi di generazione, da generazioni.csv

Nota: il vincolo "niente markdown" non e' verificabile qui, perche' genera.py
applica pulisci() prima di salvare e i blocchi markdown vengono rimossi. Per
misurarlo servirebbe salvare anche la risposta grezza.

Uso:  python statiche.py            tutti i modelli
      python statiche.py 1b         un modello solo
"""

import ast
import csv
import json
import re
import sys
from pathlib import Path

QUI = Path(__file__).parent
DATASET = QUI.parent / "benchmark" / "dataset" / "ULT_Lite.jsonl"
N_CAMPIONI = 100
MIN_TEST, MAX_TEST = 3, 8

campioni = [json.loads(r) for r in
            DATASET.read_text(encoding="utf-8").splitlines()][:N_CAMPIONI]

# registro delle generazioni: (modello, indice) -> (finish_reason, secondi)
registro = {}
with (QUI / "generazioni.csv").open(encoding="utf-8") as f:
    for r in csv.DictReader(f):
        registro[(r["modello"], int(r["indice"]))] = (r["finish_reason"], r["secondi"])


def funzioni_di_test(albero):
    return [n for n in albero.body
            if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]


def analizza(sorgente, func_name):
    """Verifica i vincoli del prompt sull'AST. Restituisce un dizionario."""
    albero = ast.parse(sorgente)
    test = funzioni_di_test(albero)

    # 1. import esplicito: from funzione import <func_name>
    import_ok = any(isinstance(n, ast.ImportFrom) and n.module == "funzione"
                    and any(a.name == func_name for a in n.names)
                    for n in ast.walk(albero))

    # 2. numero di test entro il range richiesto
    numero_ok = MIN_TEST <= len(test) <= MAX_TEST

    # 3. nomi nella forma test_<func_name>_<n>
    schema = re.compile(rf"^test_{re.escape(func_name)}_\d+$")
    nomi_ok = bool(test) and all(schema.match(t.name) for t in test)

    # 4. almeno un assert per ogni funzione di test (lettura letterale del prompt)
    assert_ok = bool(test) and all(
        any(isinstance(x, ast.Assert) for x in ast.walk(t)) for t in test)

    # 4-bis. presenza di un oracolo: assert oppure pytest.raises. Un test che
    # verifica il sollevamento di un'eccezione ha un oracolo pur non contenendo
    # un assert, e senza questa distinzione risulterebbe indebitamente bocciato.
    def ha_raises(t):
        return any(isinstance(x, ast.With) and any(
            isinstance(i.context_expr, ast.Call)
            and getattr(i.context_expr.func, "attr", "") == "raises"
            for i in x.items) for x in ast.walk(t))

    oracolo_ok = bool(test) and all(
        any(isinstance(x, ast.Assert) for x in ast.walk(t)) or ha_raises(t)
        for t in test)

    return {"n_test": len(test), "import_ok": import_ok, "numero_ok": numero_ok,
            "nomi_ok": nomi_ok, "assert_ok": assert_ok, "oracolo_ok": oracolo_ok,
            "formato_ok": import_ok and numero_ok and nomi_ok and assert_ok}


def misura(sigla):
    righe = []
    for i, campione in enumerate(campioni):
        func_name = campione["func_name"]
        percorso = QUI / "generati" / sigla / f"test_{i:03d}_{func_name}.py"
        motivo, secondi = registro.get((sigla, i), ("", ""))

        riga = {"modello": sigla, "indice": i, "func_name": func_name,
                "finish_reason": motivo, "secondi": secondi,
                "sintassi_valida": "", "n_test": "", "import_ok": "",
                "numero_ok": "", "nomi_ok": "", "assert_ok": "", "oracolo_ok": "", "formato_ok": ""}

        if not percorso.exists() or not percorso.read_text(encoding="utf-8").strip():
            # nessuna riga nel registro = il ciclo non e' mai arrivato al campione
            riga["stato"] = "non_scritto" if (sigla, i) in registro else "non_tentato"
            righe.append(riga)
            continue

        riga["stato"] = "scritto"
        sorgente = percorso.read_text(encoding="utf-8")
        try:
            esiti = analizza(sorgente, func_name)
        except SyntaxError:
            riga["sintassi_valida"] = False
            righe.append(riga)
            continue

        riga["sintassi_valida"] = True
        riga.update(esiti)
        righe.append(riga)
    return righe


def percentuale(righe, condizione, base=None):
    base = base if base is not None else righe
    return 100 * sum(1 for r in base if condizione(r)) / len(base) if base else 0.0


def riepilogo(sigla, righe):
    tentati = [r for r in righe if r["stato"] != "non_tentato"]
    scritti = [r for r in tentati if r["stato"] == "scritto"]
    validi = [r for r in scritti if r["sintassi_valida"] is True]

    print(f"\n=== {sigla}  ({len(tentati)} campioni tentati su {N_CAMPIONI}) ===")
    print(f"  scritti                 {len(scritti):3d}  "
          f"({percentuale(tentati, lambda r: r['stato'] == 'scritto'):.1f}%)")
    print(f"  sintatticamente validi  {len(validi):3d}  "
          f"({percentuale(scritti, lambda r: r['sintassi_valida'] is True):.1f}% degli scritti)")
    print(f"  risposte troncate       "
          f"{sum(1 for r in tentati if r['finish_reason'] == 'length'):3d}  "
          f"({percentuale(tentati, lambda r: r['finish_reason'] == 'length'):.1f}%)")
    if validi:
        print("  aderenza al formato (sui sintatticamente validi):")
        for chiave, etichetta in [("import_ok", "import corretto"),
                                  ("numero_ok", f"da {MIN_TEST} a {MAX_TEST} test"),
                                  ("nomi_ok", "nomi conformi"),
                                  ("assert_ok", "un assert per test"),
                                  ("oracolo_ok", "un oracolo per test"),
                                  ("formato_ok", "TUTTI i vincoli")]:
            print(f"    {etichetta:<22} {percentuale(validi, lambda r, k=chiave: r[k]):5.1f}%")
        media = sum(r["n_test"] for r in validi) / len(validi)
        print(f"    test per file (media)  {media:5.1f}")
    tempi = [float(r["secondi"]) for r in tentati if r["secondi"]]
    if tempi:
        print(f"  tempo medio di generazione {sum(tempi)/len(tempi):.1f} s")


sigle = sys.argv[1:] or ["1b", "3b", "8b"]
tutte = []
for s in sigle:
    righe = misura(s)
    tutte.extend(righe)
    riepilogo(s, righe)

colonne = ["modello", "indice", "func_name", "stato", "finish_reason", "secondi",
           "sintassi_valida", "n_test", "import_ok", "numero_ok", "nomi_ok",
           "assert_ok", "oracolo_ok", "formato_ok"]
uscita = QUI / "statiche.csv"
with uscita.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=colonne)
    w.writeheader()
    w.writerows(tutte)
print(f"\n-> {uscita.name}  ({len(tutte)} righe)")
