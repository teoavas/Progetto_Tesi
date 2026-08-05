"""Costruzione del prompt e pulizia dell'output dei modelli.

Il template e' in prompt_template.txt: e' il template "dichiarato" che va
citato in tesi. Qui viene solo riempito con i campi del campione.
"""

import re
from pathlib import Path

CARTELLA = Path(__file__).parent
TEMPLATE = (CARTELLA / "prompt_template.txt").read_text(encoding="utf-8")


def costruisci_prompt(campione: dict) -> str:
    """Riempie il template con i dati di un campione del dataset.

    Usa solo `code` e `func_name`: la descrizione in linguaggio naturale
    (campo `prompt`) non viene passata al modello, per scelta sperimentale.
    """
    return TEMPLATE.format(
        func_name=campione["func_name"],
        code=campione["code"].strip(),
    )


def pulisci_output(testo: str) -> str:
    """Estrae il codice Python dalla risposta grezza del modello.

    I modelli piccoli aggiungono spesso blocchi markdown o frasi di
    contorno, anche quando il prompt lo vieta: questa funzione normalizza
    l'output in modo che il file salvato sia sempre codice puro.
    """
    testo = testo.strip()

    # caso 1: blocco markdown ```python ... ```
    blocchi = re.findall(r"```(?:python|py)?\s*\n(.*?)```", testo, re.DOTALL)
    if blocchi:
        # se ci sono piu' blocchi si tengono tutti, in ordine
        testo = "\n\n".join(b.strip() for b in blocchi)
    else:
        # caso 2: fence aperta ma mai chiusa (troncamento)
        if testo.startswith("```"):
            testo = re.sub(r"^```(?:python|py)?\s*\n", "", testo)
            testo = testo.replace("```", "")

    # caso 3: prosa iniziale prima della prima riga di codice vera
    righe = testo.splitlines()
    for i, riga in enumerate(righe):
        if riga.startswith(("import ", "from ", "def ", "@")):
            righe = righe[i:]
            break
    return "\n".join(righe).strip() + "\n"


if __name__ == "__main__":
    # prova rapida con un campione fittizio
    esempio = {"func_name": "somma", "code": "def somma(a, b):\n    return a + b"}
    print(costruisci_prompt(esempio))
    print("=" * 60)
    sporco = (
        "Sure! Here are the unit tests:\n\n```python\n"
        "from funzione import somma\n\n"
        "def test_somma_1():\n    assert somma(1, 2) == 3\n```\n"
        "Let me know if you need more."
    )
    print(pulisci_output(sporco))
