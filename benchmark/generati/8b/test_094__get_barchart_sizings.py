from funzione import _get_barchart_sizings

def test__get_barchart_sizings_1():
    assert _get_barchart_sizings('title', 2, 2, 100) == (100, 20, 10, 'false', 25)

def test__get_barchart_sizings_2():
    assert _get_barchart_sizings('title', 5, 2, 100) == (100, 10, 10, 'false', 25)

def test__get_barchart_sizings_3():
    assert _get_barchart_sizings('title', 10, 2, 100) == (100, 6, 9, 'false', 25)

def test__get_barchart_sizings_4():
    assert _get_barchart_sizings('title', 16, 2, 100) == (100, 4, 9, 'false', 25)

def test__get_barchart_sizings_5():
    assert _get_barchart_sizings('title', 2, 2, 1200) == (1200, 20, 10, 'false', 35)

def test__get_barchart_sizings_6():
    assert _get_barchart_sizings('title', 5, 2, 1200) == (1200, 10, 10, 'false', 35)

def test__get_barchart_sizings_7():
    assert _get_barchart_sizings('title', 10, 2, 1200) == (1200, 6, 9, 'false', 35)

def test__get_barchart_sizings_8():
    assert _get_barchart_sizings('title', 16, 2, 1200) == (1200, 4, 9, 'false', 35)
