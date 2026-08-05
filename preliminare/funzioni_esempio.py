"""Funzioni semplici su cui fare esperimenti con ast e Klara.

Sono volutamente di difficolta' crescente:
1. una funzione pura senza rami
2. una con if/else (piu' cammini di esecuzione)
3. una con un ciclo e un'eccezione
"""


def somma(a, b):
    """Somma due numeri."""
    return a + b


def classifica_voto(voto):
    """Classifica un voto universitario (scala 18-30)."""
    if voto < 18:
        return "insufficiente"
    elif voto < 24:
        return "sufficiente"
    elif voto < 28:
        return "buono"
    else:
        return "ottimo"


def media_positivi(numeri):
    """Calcola la media dei soli numeri positivi di una lista.

    Solleva ValueError se non ci sono numeri positivi.
    """
    positivi = [n for n in numeri if n > 0]
    if not positivi:
        raise ValueError("nessun numero positivo")
    return sum(positivi) / len(positivi)
