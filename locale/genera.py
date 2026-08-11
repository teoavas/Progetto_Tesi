"""Versione locale con Ollama, separata dal lavoro su NVIDIA.

Stessi tre modelli (stessi pesi di Meta), eseguiti sul proprio computer.
Differenza da dichiarare in tesi: in locale sono quantizzati a 4 bit.

Prima volta, una tantum:
    ollama pull llama3.2:1b

Uso:  python genera.py 1b 0     (modello, numero del campione)
"""

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
flusso = client.chat.completions.create(
    model=MODELLI[sigla],
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    max_tokens=1024,
    stream=True,
)

pezzi = []
for blocco in flusso:
    pezzo = blocco.choices[0].delta.content or ""
    print(pezzo, end="", flush=True)
    pezzi.append(pezzo)
testo = "".join(pezzi)


def pulisci(t):
    """Toglie i blocchi markdown: i modelli li aggiungono anche se vietati."""
    blocchi = re.findall(r"```(?:python|py)?\s*\n(.*?)```", t, re.DOTALL)
    return "\n\n".join(b.strip() for b in blocchi) + "\n" if blocchi else t.strip() + "\n"


nome = f"test_{indice:03d}_{campione['func_name']}.py"
cartella = QUI / "generati" / sigla
cartella.mkdir(parents=True, exist_ok=True)
(cartella / nome).write_text(pulisci(testo), encoding="utf-8")
print(f"\n\n-> {nome}  ({time.perf_counter()-inizio:.0f}s)")
