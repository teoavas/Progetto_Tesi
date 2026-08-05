"""Genera i test per UNA funzione alla volta, con un modello alla volta.

La chiave API va messa in una variabile d'ambiente, mai nel codice:
    PowerShell:  $env:NVIDIA_API_KEY = "nvapi-..."
    cmd:         set NVIDIA_API_KEY=nvapi-...

Uso:
    python genera.py 1b 0        modello 1b, primo campione
    python genera.py 8b 5        modello 8b, sesto campione
"""

import csv
import json
import os
import sys
import time
from pathlib import Path

from openai import OpenAI

from carica_dataset import SOTTOINSIEME
from prompt import costruisci_prompt, pulisci_output

CARTELLA = Path(__file__).parent
TEMPI = CARTELLA / "results" / "tempi.csv"

MODELLI = {
    "1b": "meta/llama-3.2-1b-instruct",
    "3b": "meta/llama-3.2-3b-instruct",
    "8b": "meta/llama-3.1-8b-instruct",
}


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in MODELLI:
        raise SystemExit(f"Uso: python genera.py [{'|'.join(MODELLI)}] <indice>")
    sigla, indice = sys.argv[1], int(sys.argv[2])

    campioni = [json.loads(r) for r in
                SOTTOINSIEME.read_text(encoding="utf-8").splitlines() if r.strip()]
    campione = campioni[indice]
    testo_prompt = costruisci_prompt(campione)

    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=os.environ["NVIDIA_API_KEY"],
    )

    inizio = time.perf_counter()
    risposta = client.chat.completions.create(
        model=MODELLI[sigla],
        messages=[{"role": "user", "content": testo_prompt}],
        temperature=0,
        max_tokens=1024,
        stream=False,
    )
    durata = time.perf_counter() - inizio
    grezzo = risposta.choices[0].message.content or ""

    # salvataggio: prompt inviato, risposta grezza, codice ripulito
    base = f"{campione['task_id']}_{campione['func_name']}"
    (CARTELLA / "prompts" / sigla).mkdir(parents=True, exist_ok=True)
    (CARTELLA / "generated" / sigla).mkdir(parents=True, exist_ok=True)
    (CARTELLA / "prompts" / sigla / f"{base}.txt").write_text(
        testo_prompt, encoding="utf-8")
    (CARTELLA / "generated" / sigla / f"{base}.raw.txt").write_text(
        grezzo, encoding="utf-8")
    (CARTELLA / "generated" / sigla / f"test_{base}.py").write_text(
        pulisci_output(grezzo), encoding="utf-8")

    # tempo per generazione: serve per stimare la fattibilita' dei 100 campioni
    TEMPI.parent.mkdir(parents=True, exist_ok=True)
    nuovo = not TEMPI.exists()
    with TEMPI.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuovo:
            w.writerow(["modello", "task_id", "func_name", "secondi"])
        w.writerow([sigla, campione["task_id"], campione["func_name"],
                    round(durata, 2)])

    print(f"{sigla}  {campione['func_name']}  {durata:.2f}s")
    print(f"-> generated/{sigla}/test_{base}.py")


if __name__ == "__main__":
    main()
