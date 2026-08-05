"""Funzioni bersaglio per il ciclo di generazione test.

Volutamente piu' difficili di funzioni_brutte.py: rami annidati, eccezioni,
casi limite. Un LLM difficilmente copre tutto al primo colpo.
"""


def calcola_sconto(totale, tessera, coupon=None):
    """Calcola il prezzo finale di un carrello.

    Regole:
    - totale negativo -> ValueError
    - tessera "oro": 20% di sconto; "argento": 10%; altro/nessuna: 0%
    - coupon "BENVENUTO": -5 euro, ma solo se il totale (gia' scontato)
      supera i 30 euro; coupon sconosciuto -> ValueError
    - il prezzo finale non puo' mai scendere sotto 0
    """
    if totale < 0:
        raise ValueError("totale negativo")
    if tessera == "oro":
        prezzo = totale * 0.80
    elif tessera == "argento":
        prezzo = totale * 0.90
    else:
        prezzo = totale
    if coupon is not None:
        if coupon == "BENVENUTO":
            if prezzo > 30:
                prezzo -= 5
        else:
            raise ValueError("coupon non valido")
    if prezzo < 0:
        prezzo = 0
    return round(prezzo, 2)


def valida_password(password):
    """Valuta una password e restituisce una lista di problemi.

    Controlli: lunghezza minima 8, almeno una maiuscola, almeno una cifra,
    niente spazi, non deve essere tra quelle vietate. Lista vuota = valida.
    """
    vietate = {"password", "12345678", "qwertyuiop"}
    problemi = []
    if not isinstance(password, str):
        raise TypeError("la password deve essere una stringa")
    if len(password) < 8:
        problemi.append("troppo corta")
    if password.lower() in vietate:
        problemi.append("password troppo comune")
    if not any(c.isupper() for c in password):
        problemi.append("manca una maiuscola")
    if not any(c.isdigit() for c in password):
        problemi.append("manca una cifra")
    if " " in password:
        problemi.append("contiene spazi")
    return problemi


def interpreta_orario(testo):
    """Converte un orario scritto come testo in minuti da mezzanotte.

    Formati accettati: "HH:MM" (24h) e "H" o "HH" (ora piena).
    Esempi: "9:30" -> 570, "14" -> 840, "00:00" -> 0.
    Errori: formato non riconosciuto, ora > 23, minuti > 59 -> ValueError.
    """
    if not testo or not isinstance(testo, str):
        raise ValueError("orario mancante")
    testo = testo.strip()
    if ":" in testo:
        parti = testo.split(":")
        if len(parti) != 2 or not parti[0].isdigit() or not parti[1].isdigit():
            raise ValueError("formato non valido")
        ore, minuti = int(parti[0]), int(parti[1])
    else:
        if not testo.isdigit():
            raise ValueError("formato non valido")
        ore, minuti = int(testo), 0
    if ore > 23:
        raise ValueError("ora fuori intervallo")
    if minuti > 59:
        raise ValueError("minuti fuori intervallo")
    return ore * 60 + minuti
