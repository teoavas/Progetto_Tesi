"""Generazione dei test con i modelli Llama sul catalogo NVIDIA.

Per ogni coppia (modello, campione) invia il prompt, salva la risposta e
misura il tempo impiegato. Temperatura 0: output deterministico, una sola
generazione per campione.

La chiave API NON va scritta qui. Impostarla come variabile d'ambiente:

    Windows (PowerShell):  $env:NVIDIA_API_KEY = "nvapi-..."
    Windows (cmd):         set NVIDIA_API_KEY=nvapi-...
    Linux/macOS:           export NVIDIA_API_KEY=nvapi-...

Uso:
    python genera.py                 tutti i modelli, tutti i campioni scelti
    python genera.py --modello 1b    un modello solo
    python genera.py --limite 3      prova rapida sui primi 3 campioni
"""

import argparse
import json
import os
import time
from pathlib import Path

from openai import OpenAI

from carica_dataset import SOTTOINSIEME
from prompt import costruisci_prompt, pulisci_output

CARTELLA = Path(__file__).parent
GENERATI = CARTELLA / "generated"
PROMPTS = CARTELLA / "prompts"
REGISTRO = CARTELLA / "results" / "registro_generazioni.jsonl"

MODELLI = {
    "1b": "meta/llama-3.2-1b-instruct",
    "3b": "meta/llama-3.2-3b-instruct",
    "8b": "meta/llama-3.1-8b-instruct",
}

TEMPERATURA = 0.0
MAX_TOKENS = 1024


def crea_client() -> OpenAI:
    chiave = os.environ.get("NVIDIA_API_KEY")
    if not chiave:
        raise SystemExit(
            "Manca la variabile d'ambiente NVIDIA_API_KEY.\n"
            'PowerShell:  $env:NVIDIA_API_KEY = "nvapi-..."'
        )
    return OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=chiave)


def carica_campioni(limite: int | None = None) -> list[dict]:
    if not SOTTOINSIEME.exists():
        raise SystemExit("Esegui prima: python carica_dataset.py")
    campioni = [json.loads(r) for r in
                SOTTOINSIEME.read_text(encoding="utf-8").splitlines() if r.strip()]
    return campioni[:limite] if limite else campioni


def genera_uno(client: OpenAI, modello: str, campione: dict) -> dict:
    """Una chiamata al modello. Restituisce il record di esito."""
    testo_prompt = costruisci_prompt(campione)
    inizio = time.perf_counter()
    errore = None
    grezzo = ""
    try:
        risposta = client.chat.completions.create(
            model=modello,
            messages=[{"role": "user", "content": testo_prompt}],
            temperature=TEMPERATURA,
            max_tokens=MAX_TOKENS,
            stream=False,
        )
        grezzo = risposta.choices[0].message.content or ""
    except Exception as e:  # rete, quota, modello non disponibile...
        errore = f"{type(e).__name__}: {e}"
    durata = time.perf_counter() - inizio

    return {
        "modello": modello,
        "task_id": campione["task_id"],
        "func_name": campione["func_name"],
        "secondi": round(durata, 2),
        "errore": errore,
        "grezzo": grezzo,
    }


def salva(record: dict, sigla: str, campione: dict) -> None:
    """Salva prompt, risposta grezza e codice ripulito in file separati."""
    base = f"{record['task_id']}_{record['func_name']}"

    cartella_prompt = PROMPTS / sigla
    cartella_prompt.mkdir(parents=True, exist_ok=True)
    (cartella_prompt / f"{base}.txt").write_text(
        costruisci_prompt(campione), encoding="utf-8")

    cartella_out = GENERATI / sigla
    cartella_out.mkdir(parents=True, exist_ok=True)
    (cartella_out / f"{base}.raw.txt").write_text(record["grezzo"], encoding="utf-8")

    codice = pulisci_output(record["grezzo"]) if record["grezzo"] else ""
    (cartella_out / f"test_{base}.py").write_text(codice, encoding="utf-8")

    # la funzione sotto test, accanto ai suoi test (l'import e' "from funzione")
    (cartella_out / f"funzione_{base}.py").write_text(
        campione["code"].strip() + "\n", encoding="utf-8")

    record["formato_pulito"] = codice.strip() != record["grezzo"].strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--modello", choices=list(MODELLI), help="solo questo modello")
    ap.add_argument("--limite", type=int, help="solo i primi N campioni")
    args = ap.parse_args()

    client = crea_client()
    campioni = carica_campioni(args.limite)
    sigle = [args.modello] if args.modello else list(MODELLI)

    REGISTRO.parent.mkdir(parents=True, exist_ok=True)
    with REGISTRO.open("a", encoding="utf-8") as log:
        for sigla in sigle:
            modello = MODELLI[sigla]
            tempi = []
            print(f"\n=== {sigla} ({modello}) — {len(campioni)} campioni ===")
            for i, campione in enumerate(campioni, 1):
                rec = genera_uno(client, modello, campione)
                salva(rec, sigla, campione)
                tempi.append(rec["secondi"])
                stato = "ERRORE" if rec["errore"] else "ok"
                print(f"  [{i:>3}/{len(campioni)}] {campione['func_name'][:30]:<30} "
                      f"{rec['secondi']:>6.2f}s  {stato}")
                rec.pop("grezzo")  # nel registro non serve, sta gia' nei file
                rec["momento"] = time.strftime("%Y-%m-%d %H:%M:%S")
                log.write(json.dumps(rec, ensure_ascii=False) + "\n")
                log.flush()
            if tempi:
                medio = sum(tempi) / len(tempi)
                print(f"  media {medio:.2f}s/campione "
                      f"→ stima per 100 campioni: {medio * 100 / 60:.1f} minuti")


if __name__ == "__main__":
    main()
