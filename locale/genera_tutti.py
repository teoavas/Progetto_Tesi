"""Genera in serie, richiamando genera.py per ogni campione.

Salta i file gia' presenti: si puo' interrompere con Ctrl+C e ripartire.

Uso:
    python genera_tutti.py 8b 0 99      un modello, dai campioni 0 a 99
    python genera_tutti.py 8b 0 9 --rifai   rigenera anche se il file esiste
"""

import subprocess
import sys
from pathlib import Path

QUI = Path(__file__).parent
sigla, primo, ultimo = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
rifai = "--rifai" in sys.argv

falliti = []
for indice in range(primo, ultimo + 1):
    esistente = list((QUI / "generati" / sigla).glob(f"test_{indice:03d}_*.py"))
    if esistente and not rifai:
        print(f"[{indice:>3}] gia' presente, salto")
        continue

    print(f"[{indice:>3}] in corso...", flush=True)
    esito = subprocess.run([sys.executable, str(QUI / "genera.py"), sigla, str(indice)],
                           capture_output=True, text=True)
    if esito.returncode == 0:
        ultima = [r for r in esito.stdout.splitlines() if "File generato" in r]
        print(f"[{indice:>3}] {ultima[0].strip() if ultima else 'fatto'}")
    else:
        # Mostra il motivo: senza questo un fallimento resta muto e non si
        # distingue un problema del modello da un errore dello script.
        motivo = (esito.stderr or "").strip().splitlines()
        print(f"[{indice:>3}] FALLITO  {motivo[-1] if motivo else 'nessun messaggio'}")
        falliti.append(indice)

print(f"\nfiniti. Falliti: {falliti if falliti else 'nessuno'}")
