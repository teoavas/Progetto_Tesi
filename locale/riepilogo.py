"""Unisce le misure statiche e dinamiche e stampa le tabelle per la tesi.

Legge statiche.csv e misure_<sigla>.csv, li unisce su (modello, indice) e
riporta, per ogni modello:

  - i rami dell'albero, in percentuale sui campioni
  - Pass@1 calcolato sul singolo test, non sul file
  - copertura di riga e di ramo su tre basi diverse
  - duplicazione sulle due basi

Le tre basi della copertura rispondono a domande diverse e vanno dichiarate:
  tutti          media su tutti i campioni, copertura nulla ai non eseguibili
  eseguibili     media sui soli campioni che arrivano all'esecuzione
  import_ok      media sui soli campioni che hanno importato la funzione

La terza serve a separare l'incapacita' di scrivere test dal non aver seguito
l'istruzione sull'import: senza quell'import la funzione non viene mai chiamata
e la copertura e' nulla per costruzione.

Uso:  python riepilogo.py [1b 3b 8b]
"""

import csv
import sys
from pathlib import Path

QUI = Path(__file__).parent


def leggi(percorso):
    with percorso.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def media(righe, chiave):
    valori = [float(r[chiave]) for r in righe if r.get(chiave) not in (None, "")]
    return sum(valori) / len(valori) if valori else 0.0


def quota(righe, condizione):
    return 100 * sum(1 for r in righe if condizione(r)) / len(righe) if righe else 0.0


statiche = {(r["modello"], r["indice"]): r for r in leggi(QUI / "statiche.csv")}

for sigla in (sys.argv[1:] or ["1b", "3b", "8b"]):
    percorso = QUI / f"misure_{sigla}.csv"
    if not percorso.exists():
        print(f"\n=== {sigla}: {percorso.name} non trovato, lancia prima misura.py ===")
        continue

    righe = leggi(percorso)
    for r in righe:                      # unione con le misure statiche
        r.update({f"s_{k}": v for k, v in
                  statiche.get((sigla, r["indice"]), {}).items()})

    eseguibili = [r for r in righe if r["esito"] in ("passato", "fallito")]
    con_import = [r for r in eseguibili if r.get("s_import_ok") == "True"]

    print(f"\n=== {sigla}  ({len(righe)} campioni) ===")
    print("  esiti:")
    for stato in ("passato", "fallito", "non_eseguibile", "timeout"):
        n = sum(1 for r in righe if r["esito"] == stato)
        print(f"    {stato:<16} {n:3d}  ({quota(righe, lambda r, s=stato: r['esito'] == s):5.1f}%)")

    tot_test = sum(int(r["n_test"]) for r in righe)
    tot_pass = sum(int(r["passati"]) for r in righe)
    print(f"\n  Pass@1 (sul singolo test)  {100 * tot_pass / tot_test if tot_test else 0:.1f}%"
          f"   ({tot_pass} test corretti su {tot_test} generati)")

    print("\n  copertura, per base di calcolo:")
    print(f"    {'base':<14}{'n':>5}{'righe':>10}{'rami':>9}")
    # La base "tutti" attribuisce copertura nulla ai campioni non eseguibili,
    # perche' i loro valori sono gia' zero nel CSV.
    for nome, base in (("tutti", righe), ("eseguibili", eseguibili),
                       ("import_ok", con_import)):
        if not base:   # una base vuota e' essa stessa un'informazione
            print(f"    {nome:<14}{0:>5}{'--':>10}{'--':>9}")
            continue
        print(f"    {nome:<14}{len(base):>5}{media(base, 'cov_righe'):>9.1f}%"
              f"{media(base, 'cov_rami'):>8.1f}%")

    # dup_passati va mediata sui soli file che hanno almeno un test passato:
    # dove non ne hanno, non ci sono righe da confrontare e il valore e' zero
    # per costruzione, il che schiaccerebbe la media senza dire nulla.
    con_passati = [r for r in eseguibili if int(r["passati"]) > 0]
    if eseguibili:
        print(f"\n  duplicazione:")
        print(f"    tutti i test        {media(eseguibili, 'dup_tutti'):5.1f}%"
              f"   (su {len(eseguibili)} campioni eseguibili)")
        if con_passati:
            print(f"    solo test passati   {media(con_passati, 'dup_passati'):5.1f}%"
                  f"   (su {len(con_passati)} campioni con almeno un test passato)")
            print(f"    per confronto, tutti i test sugli stessi {len(con_passati)} campioni: "
                  f"{media(con_passati, 'dup_tutti'):.1f}%")
        else:
            print("    solo test passati      --   (nessun campione con test passati)")
