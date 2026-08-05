"""Genera gli unit test per una funzione del dataset, con un modello.

Prerequisiti:
  1. dataset/ULT_Lite.jsonl scaricato da
     https://raw.githubusercontent.com/huangd1999/UnLeakedTestBench/main/datasets/ULT_Lite.jsonl
  2. chiave API nella variabile d'ambiente (mai nel codice):
     PowerShell:  $env:NVIDIA_API_KEY = "nvapi-..."
     cmd:         set NVIDIA_API_KEY=nvapi-...

Uso:
  python genera.py 1b 0      modello 1b, primo campione del dataset
"""

import json
import os
import re
import sys
from pathlib import Path

from openai import OpenAI

CARTELLA = Path(__file__).parent
DATASET = CARTELLA / "dataset" / "ULT_Lite.jsonl"

MODELLI = {
    "1b": "meta/llama-3.2-1b-instruct",
    "3b": "meta/llama-3.2-3b-instruct",
    "8b": "meta/llama-3.1-8b-instruct",
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


def pulisci(testo):
    """Toglie blocchi markdown e prosa: i modelli piccoli li aggiungono lo stesso."""
    blocchi = re.findall(r"```(?:python|py)?\s*\n(.*?)```", testo, re.DOTALL)
    testo = "\n\n".join(b.strip() for b in blocchi) if blocchi else testo.strip()
    righe = testo.splitlines()
    for i, riga in enumerate(righe):
        if riga.startswith(("import ", "from ", "def ", "@")):
            return "\n".join(righe[i:]).strip() + "\n"
    return testo.strip() + "\n"


sigla, indice = sys.argv[1], int(sys.argv[2])
campione = [json.loads(r) for r in
            DATASET.read_text(encoding="utf-8").splitlines() if r.strip()][indice]

prompt = TEMPLATE.format(func_name=campione["func_name"],
                         code=campione["code"].strip())

client = OpenAI(base_url="https://integrate.api.nvidia.com/v1",
                api_key=os.environ["NVIDIA_API_KEY"])
risposta = client.chat.completions.create(
    model=MODELLI[sigla],
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    max_tokens=1024,
    stream=False,
)
grezzo = risposta.choices[0].message.content

uscita = CARTELLA / f"test_{sigla}_{campione['task_id']}_{campione['func_name']}.py"
uscita.write_text(pulisci(grezzo), encoding="utf-8")

print(grezzo)
print(f"\n-> salvato in {uscita.name}")
