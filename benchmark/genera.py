"""Uso:  python genera.py 3b 0     (modello, numero del campione)

Modelli serviti da NVIDIA build. La chiave sta in chiave.py (ignorato da git).
"""

import json
import re
import sys
import time
from pathlib import Path

from openai import OpenAI

from chiave import API_KEY

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


def pulisci(t):
    """Toglie i blocchi markdown: i modelli li aggiungono anche se vietati."""
    blocchi = re.findall(r"```(?:python|py)?\s*\n(.*?)```", t, re.DOTALL)
    return "\n\n".join(b.strip() for b in blocchi) + "\n" if blocchi else t.strip() + "\n"


QUI = Path(__file__).parent
sigla, indice = sys.argv[1], int(sys.argv[2])

righe = (QUI / "dataset" / "ULT_Lite.jsonl").read_text(encoding="utf-8").splitlines()
campione = json.loads(righe[indice])
prompt = TEMPLATE.format(func_name=campione["func_name"], code=campione["code"].strip())

print(f"chiamo {MODELLI[sigla]} su {campione['func_name']}...")
inizio = time.perf_counter()

client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=API_KEY,
                timeout=180, max_retries=0)
completion = client.chat.completions.create(
    model=MODELLI[sigla],
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
    stream=False,
)
testo = completion.choices[0].message.content

nome = f"test_{sigla}_{campione['task_id']}.py"
(QUI / nome).write_text(pulisci(testo), encoding="utf-8")
print(testo)
print(f"\n-> {nome}  ({time.perf_counter()-inizio:.0f}s)")
