from funzione import _get_barchart_sizings

def test__get_barchart_sizings_1():
    result = _get_barchart_sizings('x_title', 3, 5, 100)
    assert result[0] == 450
    assert result[1] == 10
    assert result[2] == 9
    assert result[3] == 'false'
    assert result[4] == 35

def test__get_barchart_sizings_2():
    result = _get_barchart_sizings('x_title', 7, 5, 100)
    assert result[0] == 450
    assert result[1] == 6
    assert result[2] == 9
    assert result[3] == 'false'
    assert result[4] == 35

def test__get_barchart_sizings_3():
    result = _get_barchart_sizings('x_title', 15, 5, 100)
    assert result[0] == 450
    assert result[1] == 4
    assert result[2] == 9
    assert result[3] == 'false'
    assert result[4] == 35

def test__get_barchart_sizings_4():
    result = _get_barchart_sizings('x_title', 15, 5, 1200)
    assert result[0] == 1200
    assert result[1] == 4
    assert result[2] == 9
    assert result[3] == 'false'
    assert result[4] == 35

def test__get_barchart_sizings_5():
    result = _get_barchart_sizings('x_title', 15, 5, 100)
    assert result[0] == 450
    assert result[1] == 4
    assert result[2] == 9
    assert result[3] == 'false'
    assert result[4] == 35

def test__get_barchart_sizings_6():
    result = _get_barchart_sizings('x_title', 15, 5, 100)
    assert result[0] == 450
    assert result[1] == 4
    assert result[2] == 9
    assert result[3] == 'false'
    assert result[4] == 35

def test__get_barchart_sizings_7():
    result = _get_barchart_sizings('x_title', 15, 5, 100)
    assert result[0] == 450
    assert result[1] == 4
    assert result[2] == 9
    assert result[3] == 'false'
    assert result[4] == 35

def test__get_barchart_sizings_8():
    result = _get_barchart_sizings('x_title', 15, 5, 100)
    assert result[0] == 450
    assert result[1] == 4
    assert result[2] == 9
    assert result[3] == 'false'
    assert result[4] == 35
