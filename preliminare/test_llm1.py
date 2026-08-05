import pytest

from funzioni_esempio import media_positivi, somma, classifica_voto


# --- Casi base ---

def test_tutti_positivi():
    assert media_positivi([1, 2, 3]) == 2.0

def test_misti_positivi_e_negativi():
    # ignora -5 e -1: media di 4 e 6
    assert media_positivi([-5, 4, -1, 6]) == 5.0

def test_un_solo_positivo():
    assert media_positivi([7]) == 7.0

def test_lo_zero_viene_escluso():
    # 0 non è positivo: media solo di 10
    assert media_positivi([0, 10]) == 10.0

def test_float():
    assert media_positivi([1.5, 2.5, -3.0]) == pytest.approx(2.0)


# --- Casi di errore ---

def test_lista_vuota():
    with pytest.raises(ValueError, match="nessun numero positivo"):
        media_positivi([])

def test_tutti_negativi():
    with pytest.raises(ValueError, match="nessun numero positivo"):
        media_positivi([-1, -2, -3])

def test_solo_zeri():
    with pytest.raises(ValueError, match="nessun numero positivo"):
        media_positivi([0, 0])


# --- Casi particolari ---

def test_input_non_modificato():
    dati = [3, -1, 5]
    media_positivi(dati)
    assert dati == [3, -1, 5]

def test_funziona_con_generatori():
    assert media_positivi(x for x in [-2, 4, 8]) == 6.0

def test_valori_grandi():
    assert media_positivi([1e15, 3e15]) == 2e15


# --- somma ---

def test_somma_interi():
    assert somma(2, 3) == 5

def test_somma_negativi():
    assert somma(-2, -3) == -5

def test_somma_con_zero():
    assert somma(0, 7) == 7

def test_somma_float():
    assert somma(0.1, 0.2) == pytest.approx(0.3)

def test_somma_commutativa():
    assert somma(4, 9) == somma(9, 4)


# --- classifica_voto ---

@pytest.mark.parametrize("voto, atteso", [
    (0, "insufficiente"),
    (17, "insufficiente"),   # limite superiore insufficiente
    (18, "sufficiente"),     # confine: 18 è sufficiente
    (23, "sufficiente"),
    (24, "buono"),           # confine: 24 è buono
    (27, "buono"),
    (28, "ottimo"),          # confine: 28 è ottimo
    (30, "ottimo"),
])
def test_classifica_voto(voto, atteso):
    assert classifica_voto(voto) == atteso

def test_classifica_voto_float_sul_confine():
    assert classifica_voto(23.5) == "sufficiente"
    assert classifica_voto(27.9) == "buono"