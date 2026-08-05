"""Funzioni semplificate per Klara.

Klara (2021) supporta un sottoinsieme limitato di Python: funziona bene con
aritmetica e if/else su interi, ma va in crash con list comprehension,
eccezioni, f-string ecc. Qui teniamo solo cio' che riesce ad analizzare.
"""


def somma(a: int, b: int) -> int:
    return a + b


def classifica_voto(voto: int) -> int:
    # versione semplificata che ritorna un codice numerico
    if voto < 18:
        return 0
    elif voto < 24:
        return 1
    elif voto < 28:
        return 2
    else:
        return 3


def valore_assoluto(x: int) -> int:
    if x < 0:
        return -x
    return x
