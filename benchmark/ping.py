"""Una chiamata breve al modello indicato. Uso: python ping.py 70b"""
import sys
import time

from openai import OpenAI

from chiave import API_KEY

NOMI = {"1b": "meta/llama-3.2-1b-instruct",
        "3b": "meta/llama-3.2-3b-instruct",
        "8b": "meta/llama-3.1-8b-instruct",
        "70b": "meta/llama-3.3-70b-instruct"}

nome = NOMI[sys.argv[1]]
client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=API_KEY,
                timeout=60, max_retries=0)
inizio = time.perf_counter()
try:
    r = client.chat.completions.create(
        model=nome,
        messages=[{"role": "user", "content": "how many days are in february?"}],
        temperature=0.2, top_p=0.7, max_tokens=50,
    )
    print(f"OK   {nome} ({time.perf_counter()-inizio:.0f}s): {r.choices[0].message.content[:60]!r}")
except Exception as e:
    print(f"FAIL {nome} ({time.perf_counter()-inizio:.0f}s): {type(e).__name__}")
