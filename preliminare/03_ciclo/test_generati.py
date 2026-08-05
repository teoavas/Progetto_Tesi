import pytest
from funzioni_brutte import calcola_sconto, valida_password, interpreta_orario


# ============ calcola_sconto ============

# --- tessere ---
def test_sconto_oro():
    assert calcola_sconto(100, "oro") == 80.0

def test_sconto_argento():
    assert calcola_sconto(100, "argento") == 90.0

def test_nessuna_tessera():
    assert calcola_sconto(100, None) == 100

def test_tessera_sconosciuta_nessuno_sconto():
    assert calcola_sconto(100, "bronzo") == 100

def test_totale_zero():
    assert calcola_sconto(0, "oro") == 0

# --- coupon ---
def test_coupon_benvenuto_applicato():
    # 50 senza tessera -> 50 > 30 -> 45
    assert calcola_sconto(50, None, coupon="BENVENUTO") == 45.0

def test_coupon_su_prezzo_gia_scontato():
    # 50 oro -> 40 > 30 -> 35
    assert calcola_sconto(50, "oro", coupon="BENVENUTO") == 35.0

def test_coupon_non_applicato_sotto_soglia():
    # 25 <= 30: niente -5
    assert calcola_sconto(25, None, coupon="BENVENUTO") == 25

def test_coupon_soglia_esattamente_30():
    # serve "supera i 30": a 30 esatti niente sconto
    assert calcola_sconto(30, None, coupon="BENVENUTO") == 30

def test_coupon_soglia_dopo_tessera():
    # 33 argento -> 29.7 <= 30: coupon non applicato
    assert calcola_sconto(33, "argento", coupon="BENVENUTO") == 29.7

def test_coupon_sconosciuto():
    with pytest.raises(ValueError, match="coupon non valido"):
        calcola_sconto(100, "oro", coupon="SCONTO50")

# --- errori e arrotondamento ---
def test_totale_negativo():
    with pytest.raises(ValueError, match="totale negativo"):
        calcola_sconto(-1, "oro")

def test_arrotondamento_due_decimali():
    # 33.33 argento -> 29.997 -> 30.0
    assert calcola_sconto(33.33, "argento") == 30.0

def test_risultato_mai_negativo():
    assert calcola_sconto(0, None, coupon="BENVENUTO") >= 0


# ============ valida_password ============

def test_password_valida():
    assert valida_password("Abcdef12") == []

def test_non_stringa():
    with pytest.raises(TypeError, match="deve essere una stringa"):
        valida_password(12345678)

def test_troppo_corta():
    assert "troppo corta" in valida_password("Ab1")

def test_lunghezza_esattamente_8_ok():
    assert "troppo corta" not in valida_password("Abcdef12")

def test_password_comune():
    assert "password troppo comune" in valida_password("12345678")

def test_password_comune_case_insensitive():
    # "PASSWORD".lower() e' vietata
    assert "password troppo comune" in valida_password("PASSWORD")

def test_manca_maiuscola():
    assert "manca una maiuscola" in valida_password("abcdef12")

def test_manca_cifra():
    assert "manca una cifra" in valida_password("Abcdefgh")

def test_contiene_spazi():
    assert "contiene spazi" in valida_password("Abc def12")

def test_problemi_multipli():
    problemi = valida_password("abc")
    assert set(problemi) == {"troppo corta", "manca una maiuscola", "manca una cifra"}

def test_stringa_vuota():
    assert set(valida_password("")) == {"troppo corta", "manca una maiuscola", "manca una cifra"}


# ============ interpreta_orario ============

# --- formati validi ---
@pytest.mark.parametrize("testo, atteso", [
    ("9:30", 570),
    ("14", 840),
    ("00:00", 0),
    ("23:59", 1439),   # massimo valido
    ("0", 0),
    ("9:05", 545),
    ("9:5", 545),      # minuti a una cifra
])
def test_orari_validi(testo, atteso):
    assert interpreta_orario(testo) == atteso

def test_spazi_intorno():
    assert interpreta_orario("  9:30  ") == 570

# --- errori ---
@pytest.mark.parametrize("testo", ["", None, 930])
def test_input_mancante_o_non_stringa(testo):
    with pytest.raises(ValueError, match="orario mancante"):
        interpreta_orario(testo)

@pytest.mark.parametrize("testo", [
    "abc",        # non numerico
    "9:xx",       # minuti non numerici
    "9:30:00",    # troppe parti
    ":30",        # ore mancanti
    "9:",         # minuti mancanti
    "-5",         # negativo (isdigit falso)
    "9.30",       # separatore sbagliato
])
def test_formato_non_valido(testo):
    with pytest.raises(ValueError, match="formato non valido"):
        interpreta_orario(testo)

def test_ora_fuori_intervallo():
    with pytest.raises(ValueError, match="ora fuori intervallo"):
        interpreta_orario("24:00")

def test_ora_piena_fuori_intervallo():
    with pytest.raises(ValueError, match="ora fuori intervallo"):
        interpreta_orario("25")

def test_minuti_fuori_intervallo():
    with pytest.raises(ValueError, match="minuti fuori intervallo"):
        interpreta_orario("12:60")