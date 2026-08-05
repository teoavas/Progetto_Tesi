"""Esperimento 1: la libreria `ast` della standard library.

Obiettivo (dalla mail della prof): capire come estrarre informazioni "di alto
livello" da un file Python, da passare come contesto a un LLM invece del file
intero.

Cosa fa questo script:
1. Fa il parsing di funzioni_esempio.py in un Abstract Syntax Tree (AST)
2. Estrae per ogni funzione: nome, argomenti, docstring, return, if, raise
3. Stampa un "riassunto strutturale" del file - questo e' esattamente il tipo
   di contesto compatto che potremmo dare all'LLM

Eseguire con: python3 prova_ast.py
"""

import ast
from pathlib import Path

SORGENTE = Path(__file__).parent.parent / "funzioni_esempio.py"


def analizza_funzione(nodo: ast.FunctionDef) -> dict:
    """Estrae informazioni utili da una funzione dell'AST."""
    info = {
        "nome": nodo.name,
        "argomenti": [a.arg for a in nodo.args.args],
        "docstring": ast.get_docstring(nodo),
        "num_return": 0,
        "num_if": 0,
        "eccezioni": [],
        "riga_inizio": nodo.lineno,
        "riga_fine": nodo.end_lineno,
    }
    # ast.walk visita tutti i nodi discendenti
    for figlio in ast.walk(nodo):
        if isinstance(figlio, ast.Return):
            info["num_return"] += 1
        elif isinstance(figlio, ast.If):
            info["num_if"] += 1
        elif isinstance(figlio, ast.Raise):
            # proviamo a recuperare il nome dell'eccezione sollevata
            exc = figlio.exc
            if isinstance(exc, ast.Call) and isinstance(exc.func, ast.Name):
                info["eccezioni"].append(exc.func.id)
    return info


def main():
    codice = SORGENTE.read_text()
    albero = ast.parse(codice)

    print(f"=== Analisi AST di {SORGENTE.name} ===\n")

    for nodo in ast.walk(albero):
        if isinstance(nodo, ast.FunctionDef):
            info = analizza_funzione(nodo)
            print(f"Funzione: {info['nome']}({', '.join(info['argomenti'])})")
            print(f"  righe {info['riga_inizio']}-{info['riga_fine']}")
            print(f"  docstring: {info['docstring'].splitlines()[0] if info['docstring'] else '-'}")
            print(f"  return: {info['num_return']}, if: {info['num_if']}, "
                  f"eccezioni: {info['eccezioni'] or 'nessuna'}")
            # Nota per la tesi: num_if e' legato al numero di cammini da
            # coprire con i test -> suggerisce QUANTI test servono
            print()

    # Bonus: l'AST completo "grezzo", per capire com'e' fatto davvero
    print("=== AST grezzo della funzione 'somma' (ast.dump) ===")
    for nodo in albero.body:
        if isinstance(nodo, ast.FunctionDef) and nodo.name == "somma":
            print(ast.dump(nodo, indent=2))


if __name__ == "__main__":
    main()
