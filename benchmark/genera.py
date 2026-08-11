"""
Uso:  python genera.py 3b 0     (modello, numero del campione)

Genera test unitari usando modelli NVIDIA Integrate API.
"""

import csv
import json
import re
import sys
import time
from pathlib import Path

from openai import OpenAI
from chiave import API_KEY

# Modelli disponibili
TENTATIVI = 40   # il servizio NVIDIA e' intermittente: si insiste
PAUSA = 15       # secondi fra un tentativo e l'altro

MODELLI = {
    "1b": "meta/llama-3.2-1b-instruct",
    "3b": "meta/llama-3.2-3b-instruct",
    "8b": "meta/llama-3.1-8b-instruct",
    "70b": "meta/llama-3.3-70b-instruct",  # solo controllo
}

# Prompt template
TEMPLATE = """[instruction]
Write unit tests in Python for the function given below.
Rules:
- Use pytest style: plain functions, no classes.
- Import the function under test with: from funzione import {func_name}
- Write between 3 and 8 test functions, named test_{func_name}_1, test_{func_name}_2, and so on.
- Every test function must contain at least one assert statement.
- Do not rewrite or redefine the function under test.
- Do not write explanations, comments or markdown. Output Python code only.

[data]
{code}

[format]
from funzione import {func_name}

def test_{func_name}_1():
    assert {func_name}(...) == ...
"""

def pulisci(testo):
    """Rimuove blocchi markdown e restituisce solo il codice."""
    blocchi = re.findall(r"```(?:python|py)?\s*\n(.*?)```", testo, re.DOTALL)
    if blocchi:
        return "\n\n".join(b.strip() for b in blocchi) + "\n"
    # risposta troncata: fence aperto e mai chiuso
    testo = re.sub(r"^\s*```(?:python|py)?\s*\n", "", testo)
    return testo.strip() + "\n"


# --- MAIN ---

QUI = Path(__file__).parent
sigla, indice = sys.argv[1], int(sys.argv[2])

# Carica dataset
righe = (QUI / "dataset" / "ULT_Lite.jsonl").read_text(encoding="utf-8").splitlines()
campione = json.loads(righe[indice])

prompt = TEMPLATE.format(
    func_name=campione["func_name"],
    code=campione["code"].strip()
)

print(f"Chiamo {MODELLI[sigla]} sul task {campione['func_name']}...")
inizio = time.perf_counter()

# Client NVIDIA
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY,
    timeout=20,
    max_retries=3
)

# Tentativi limitati
testo = None
for tentativo in range(1, TENTATIVI + 1):
    print(f"  Tentativo {tentativo}...", end="", flush=True)
    try:
        completion = client.chat.completions.create(
            model=MODELLI[sigla],
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=1024,
            stream=False,
        )
        testo = completion.choices[0].message.content
        motivo = completion.choices[0].finish_reason  # "stop" = finito, "length" = troncato
        print(f" OK ({motivo})")
        break

    except Exception as e:
        print(f" ERRORE: {e}")
        time.sleep(PAUSA)

if testo is None:
    raise SystemExit("Errore: nessuna risposta dopo 6 tentativi.")

# Salva file
nome = f"test_{indice:03d}_{campione['func_name']}.py"
cartella = QUI / "generati" / sigla
cartella.mkdir(parents=True, exist_ok=True)
(cartella / nome).write_text(pulisci(testo), encoding="utf-8")

# Registro: una riga per generazione (serve per distinguere i troncamenti)
registro = QUI / "generazioni.csv"
nuovo = not registro.exists()
with registro.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    if nuovo:
        w.writerow(["modello", "indice", "func_name", "finish_reason",
                    "tentativi", "secondi"])
    w.writerow([sigla, indice, campione["func_name"], motivo, tentativo,
                round(time.perf_counter() - inizio, 1)])

print("\n--- RISPOSTA MODELLO ---")
print(testo)
print(f"\n-> File generato: generati/{sigla}/{nome}  (tempo: {time.perf_counter()-inizio:.1f}s)")
