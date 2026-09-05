"""Categorizza i test falliti leggendo i report di pytest salvati da misura.py.

Per ogni test fallito estrae la causa dal blocco delle FAILURES e la classifica
con il nome dell'eccezione. La distinzione che conta:

  AssertionError   il test ha chiamato la funzione e l'ha eseguita, ma il valore
                   atteso era sbagliato. E' il problema dell'oracolo.
  tutto il resto   il test non e' arrivato a esercitare la funzione come si
                   deve: NameError se non l'ha importata, TypeError se ha
                   sbagliato gli argomenti, e cosi' via.

Produce fallimenti.csv (una riga per test fallito) e stampa il riepilogo.

Uso:  python fallimenti.py [1b 3b 8b]
"""

import collections
import csv
import re
import sys
from pathlib import Path

QUI = Path(__file__).parent

# pytest separa i test falliti con  ______ nome_del_test ______
BLOCCO = re.compile(r"^_{3,} (.+?) _{3,}$", re.MULTILINE)
# righe della spiegazione:  E   NameError: name 'x' is not defined
# Il prefisso e' facoltativo perche' esiste anche l'eccezione nuda "Exception".
ECCEZIONE = re.compile(
    r"^E\s+((?:[A-Za-z_][\w.]*)?(?:Error|Exception|Warning))\b\s*:?\s*(.*)",
    re.MULTILINE)
# riga di traceback:  funzione.py:5: in get_segment_directions
ORIGINE = re.compile(r"^(\S+\.py):\d+: in ", re.MULTILINE)
ASSERT_NUDO = re.compile(r"^E\s+(assert\b.*)", re.MULTILINE)
NON_SOLLEVATA = re.compile(r"^E\s+Failed: DID NOT RAISE\b", re.MULTILINE)


def origine(blocco):
    """Dove l'errore e' stato sollevato: nel test o dentro la funzione.

    L'ultimo file citato nel traccia dello stack e' quello in cui l'eccezione
    e' nata. Se e' funzione.py, il test ha davvero chiamato la funzione ed e'
    stata lei a rifiutare l'input; se e' il file di test, il test non e'
    arrivato a esercitarla come si deve.
    """
    file = ORIGINE.findall(blocco)
    if not file:
        return ""
    return "funzione" if file[-1].startswith("funzione") else "test"


def categoria(blocco):
    """Causa del fallimento: la prima spiegazione utile del blocco."""
    if NON_SOLLEVATA.search(blocco):
        # il test si aspettava un'eccezione che non e' arrivata: e' comunque
        # un'aspettativa sbagliata sul comportamento, quindi un oracolo errato
        return "DID NOT RAISE", "eccezione attesa e non sollevata"
    ecc = ECCEZIONE.search(blocco)
    nudo = ASSERT_NUDO.search(blocco)
    if ecc and (not nudo or ecc.start() < nudo.start()):
        return ecc.group(1), ecc.group(2).strip()[:120]
    if nudo:
        return "AssertionError", nudo.group(1).strip()[:120]
    return "non classificato", ""


def analizza(sigla):
    righe = []
    cartella = QUI / "report" / sigla
    for percorso in sorted(cartella.glob("*.txt")):
        testo = percorso.read_text(encoding="utf-8", errors="replace")
        if "= FAILURES =" not in testo:
            continue
        sezione = testo.split("= FAILURES =", 1)[1]
        sezione = re.split(r"^=+ (?:ERRORS|warnings summary|short test summary)",
                           sezione, maxsplit=1, flags=re.MULTILINE)[0]

        tagli = list(BLOCCO.finditer(sezione))
        for i, m in enumerate(tagli):
            fine = tagli[i + 1].start() if i + 1 < len(tagli) else len(sezione)
            blocco = sezione[m.end():fine]
            tipo, messaggio = categoria(blocco)
            righe.append({"modello": sigla, "indice": int(percorso.stem),
                          "test": m.group(1), "categoria": tipo,
                          "origine": origine(blocco), "messaggio": messaggio})
    return righe


tutte = []
for sigla in (sys.argv[1:] or ["1b", "3b", "8b"]):
    righe = analizza(sigla)
    tutte.extend(righe)
    if not righe:
        print(f"\n=== {sigla}: nessun report con fallimenti ===")
        continue

    conteggio = collections.Counter(r["categoria"] for r in righe)
    # Il test ha esercitato la funzione se l'assert e' fallito, se l'eccezione
    # attesa non e' arrivata, oppure se l'errore e' nato dentro la funzione.
    raggiunta = [r for r in righe
                 if r["categoria"] in ("AssertionError", "DID NOT RAISE")
                 or r["origine"] == "funzione"]
    oracolo = len(raggiunta)
    print(f"\n=== {sigla}  ({len(righe)} test falliti) ===")
    for tipo, n in conteggio.most_common():
        print(f"    {tipo:<22} {n:4d}  ({100 * n / len(righe):5.1f}%)")
    print(f"    {'-' * 44}")
    print(f"    la funzione viene eseguita  {oracolo:4d}  "
          f"({100 * oracolo / len(righe):5.1f}%)   -> errore di oracolo")
    print(f"    la funzione non si raggiunge{len(righe) - oracolo:4d}  "
          f"({100 * (len(righe) - oracolo) / len(righe):5.1f}%)   -> errore d'uso")

# Il CSV viene riscritto per intero: lanciando lo script su un solo modello si
# perderebbero le righe degli altri, quindi in quel caso si usa un nome diverso.
if tutte:
    parziale = len(sys.argv) > 1
    uscita = QUI / ("fallimenti_%s.csv" % "_".join(sys.argv[1:]) if parziale
                    else "fallimenti.csv")
    with uscita.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["modello", "indice", "test",
                                          "categoria", "origine", "messaggio"])
        w.writeheader()
        w.writerows(tutte)
    print(f"\n-> {uscita.name}  ({len(tutte)} righe)")
