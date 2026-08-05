"""Caricamento del dataset ULT_Lite e selezione dei campioni.

Il file ULT_Lite.jsonl va scaricato a mano e messo in dataset/:
https://raw.githubusercontent.com/huangd1999/UnLeakedTestBench/main/datasets/ULT_Lite.jsonl

Selezione: i primi N campioni nell'ordine del file (criterio deterministico
e riproducibile). Per un campionamento casuale, usare `random.Random(SEED)`
e dichiarare il seed in tesi.
"""

import json
from pathlib import Path

CARTELLA = Path(__file__).parent
DATASET = CARTELLA / "dataset" / "ULT_Lite.jsonl"
SOTTOINSIEME = CARTELLA / "dataset" / "campioni_selezionati.jsonl"
N_CAMPIONI = 20


def carica_tutti() -> list[dict]:
    """Legge il file JSONL completo."""
    if not DATASET.exists():
        raise SystemExit(
            f"Manca il dataset: {DATASET}\n"
            "Scaricalo da:\n"
            "https://raw.githubusercontent.com/huangd1999/UnLeakedTestBench"
            "/main/datasets/ULT_Lite.jsonl"
        )
    campioni = []
    for riga in DATASET.read_text(encoding="utf-8").splitlines():
        riga = riga.strip()
        if riga:
            campioni.append(json.loads(riga))
    return campioni


def seleziona(n: int = N_CAMPIONI) -> list[dict]:
    """Restituisce i primi n campioni e li salva in un file separato."""
    campioni = carica_tutti()[:n]
    SOTTOINSIEME.parent.mkdir(parents=True, exist_ok=True)
    with SOTTOINSIEME.open("w", encoding="utf-8") as f:
        for c in campioni:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    return campioni


if __name__ == "__main__":
    tutti = carica_tutti()
    scelti = seleziona()
    print(f"campioni nel dataset: {len(tutti)}")
    print(f"campioni selezionati: {len(scelti)} -> {SOTTOINSIEME.name}")
    print()
    for c in scelti:
        righe = len(c["code"].strip().splitlines())
        print(f"  task_id={c['task_id']:>4}  {c['func_name'][:35]:<35} "
              f"{righe:>3} righe  {len(c.get('test_list', []))} gold test")
