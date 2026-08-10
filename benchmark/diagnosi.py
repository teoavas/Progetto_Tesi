"""Cambia una variabile alla volta per capire cosa fa fallire la chiamata."""
import json
import time
from pathlib import Path

from openai import OpenAI

from chiave import API_KEY

MODELLO = "meta/llama-3.2-3b-instruct"
QUI = Path(__file__).parent
campione = json.loads((QUI / "dataset" / "ULT_Lite.jsonl").read_text(encoding="utf-8").splitlines()[0])
TEMPLATE = (QUI / "genera.py").read_text(encoding="utf-8").split('TEMPLATE = """')[1].split('"""')[0]
lungo = TEMPLATE.format(func_name=campione["func_name"], code=campione["code"].strip())
corto = "how many days are in february?"

client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=API_KEY,
                timeout=90, max_retries=0)

prove = [
    ("A  corto, temp 0.2, max 50   (controllo)", corto, 0.2, 50),
    ("B  corto, temp 0,   max 50   (isola temperatura)", corto, 0, 50),
    ("C  corto, temp 0.2, max 1024 (isola max_tokens)", corto, 0.2, 1024),
    ("D  LUNGO, temp 0.2, max 1024 (isola prompt)", lungo, 0.2, 1024),
]

for etichetta, testo, temp, maxtok in prove:
    inizio = time.perf_counter()
    try:
        r = client.chat.completions.create(
            model=MODELLO,
            messages=[{"role": "user", "content": testo}],
            temperature=temp, top_p=0.7, max_tokens=maxtok,
        )
        n = len(r.choices[0].message.content)
        print(f"OK   {etichetta}  {time.perf_counter()-inizio:.0f}s, {n} caratteri")
    except Exception as e:
        print(f"FAIL {etichetta}  {time.perf_counter()-inizio:.0f}s, {type(e).__name__}")
