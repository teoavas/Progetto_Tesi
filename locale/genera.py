"""Generazione in locale con Ollama (stessi modelli, eseguiti sul proprio pc).

I pesi sono gli stessi rilasciati da Meta e serviti da NVIDIA; in locale sono
quantizzati a 4 bit, differenza da dichiarare in tesi.

Una tantum:
    ollama pull llama3.2:1b
    ollama pull llama3.2:3b
    ollama pull llama3.1:8b

Uso:  python genera.py 1b 0        un campione
      python genera_tutti.py 1b 0 99   i primi 100 campioni
"""


import csv
import json
import re
import sys
import time
from pathlib import Path

from openai import OpenAI

MODELLI = {
    "1b": "llama3.2:1b",
    "3b": "llama3.2:3b",
    "8b": "llama3.1:8b",
}

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

QUI = Path(__file__).parent
DATASET = QUI.parent / "benchmark" / "dataset" / "ULT_Lite.jsonl"
sigla, indice = sys.argv[1], int(sys.argv[2])

campione = json.loads(DATASET.read_text(encoding="utf-8").splitlines()[indice])
prompt = TEMPLATE.format(func_name=campione["func_name"], code=campione["code"].strip())

print(f"chiamo {MODELLI[sigla]} su {campione['func_name']}...\n")
inizio = time.perf_counter()

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama",
                timeout=600, max_retries=0)
completion = client.chat.completions.create(
    model=MODELLI[sigla],
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    max_tokens=1024,
    stream=False,
)
testo = completion.choices[0].message.content
motivo = completion.choices[0].finish_reason  # "stop" = finito, "length" = troncato
print(testo)


def pulisci(t):
    """Toglie i blocchi markdown: i modelli li aggiungono anche se vietati."""
    blocchi = re.findall(r"```(?:python|py)?\s*\n(.*?)```", t, re.DOTALL)
    return "\n\n".join(b.strip() for b in blocchi) + "\n" if blocchi else t.strip() + "\n"


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
        w.writerow(["modello", "indice", "func_name", "finish_reason", "secondi"])
    w.writerow([sigla, indice, campione["func_name"], motivo,
                round(time.perf_counter() - inizio, 1)])

print(f"\n-> generati/{sigla}/{nome}  ({motivo}, {time.perf_counter()-inizio:.0f}s)")
