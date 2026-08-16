from funzione import _get_barchart_sizings

def test__get_barchart_sizings_1():
    assert _get_barchart_sizings('test', 3, 2, 100) == (300, 10, 9, 'true', 25)

def test__get_barchart_sizings_2():
    assert _get_barchart_sizings('test', 1, 1, 100) == (120, 20, 10, 'false', 35)

def test__get_barchart_sizings_3():
    assert _get_barchart_sizings('test', 5, 2, 200) == (300, 8, 9, 'true', 25)

def test__get_barchart_sizings_4():
    assert _get_barchart_sizings('test', 10, 3, 250) == (450, 6, 8, 'true', 35)

def test__get_barchart_sizings_5():
    assert _get_barchart_sizings('test', 16, 4, 300) == (400, 4, 9, 'true', 25)

def test__get_barchart_sizings_6():
    with pytest.raises(ValueError):
        _get_barchart_sizings('test', -1, 2, 100)

def test__get_barchart_sizings_7():
    assert _get_barchart_sizings('test', 3, 0, 100) == (120, 20, 10, 'false', 35)

def test__get_barchart_sizings_8():
    with pytest.raises(ValueError):
        _get_barchart_sizings('test', 3, 2, -1)
