"""Diagnostica: quali llama esistono e quali rispondono. Uso: python prova.py"""

from openai import OpenAI

from chiave import API_KEY

client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=API_KEY,
                timeout=30, max_retries=0)

print("1) modelli con 'llama-3' nel nome:")
for m in client.models.list():
    if "llama-3" in m.id:
        print("   -", m.id)

print("\n2) prova di generazione su piu' modelli (5 token ciascuno):")
for nome in ["meta/llama-3.2-1b-instruct",
             "meta/llama-3.2-3b-instruct",
             "meta/llama-3.1-8b-instruct",
             "mistralai/mistral-7b-instruct-v0.3",
             "microsoft/phi-3-mini-4k-instruct"]:
    try:
        r = client.chat.completions.create(
            model=nome,
            messages=[{"role": "user", "content": "say hi"}],
            max_tokens=5,
        )
        print(f"   OK   {nome}: {r.choices[0].message.content!r}")
    except Exception as e:
        print(f"   FAIL {nome}: {type(e).__name__}")
