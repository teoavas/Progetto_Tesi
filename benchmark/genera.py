"""Uso:  python genera.py 1b 0     (modello, numero del campione)"""

import json
import sys
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

QUI = Path(__file__).parent
sigla, indice = sys.argv[1], int(sys.argv[2])

righe = (QUI / "dataset" / "ULT_Lite.jsonl").read_text(encoding="utf-8").splitlines()
campione = json.loads(righe[indice])
prompt = TEMPLATE.format(func_name=campione["func_name"], code=campione["code"].strip())

print(f"chiamo {MODELLI[sigla]} su {campione['func_name']}...\n")

client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=API_KEY,
                timeout=180, max_retries=0)
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

nome = f"test_{sigla}_{campione['task_id']}.py"
(QUI / nome).write_text(testo, encoding="utf-8")
print("\n\n-> salvato in", nome)
