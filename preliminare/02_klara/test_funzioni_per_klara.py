import funzioni_per_klara


def test_somma_0():
    assert funzioni_per_klara.somma(0, 0) == 0


def test_classifica_voto_0():
    assert funzioni_per_klara.classifica_voto(0) == 0
    assert funzioni_per_klara.classifica_voto(18) == 1
    assert funzioni_per_klara.classifica_voto(24) == 2
    assert funzioni_per_klara.classifica_voto(28) == 3


def test_valore_assoluto_0():
    assert funzioni_per_klara.valore_assoluto(-1) == 1
    assert funzioni_per_klara.valore_assoluto(0) == 0
