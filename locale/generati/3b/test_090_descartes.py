from funzione import descartes

def test_descartes_1():
    assert descartes([1, -2, 3]) == [[0, 0, 2], [1, 0, 1]]

def test_descartes_2():
    assert descartes([-1, 2, -3]) == [[0, 0, 2], [1, 0, 1]]

def test_descartes_3():
    assert descartes([1, -1, 1]) == [[0, 0, 1], [1, 0, 0]]

def test_descartes_4():
    assert descartes([-2, 1, -3]) == [[0, 0, 2], [1, 0, 1]]

def test_descartes_5():
    assert descartes([1, -2, -3]) == []

def test_descartes_6():
    assert descartes([-1, -2, -3]) == [[0, 0, 3], [1, 0, 2]]

def test_descartes_7():
    assert descartes([1, 2, 3]) == []
