from funzione import descartes

def test_descartes_1():
    poly_array = [2, 0, -3, 0, 4]
    expected_output = [[0, 0, 5], [1, 0, 4]]
    assert descartes(poly_array) == expected_output

def test_descartes_2():
    poly_array = [-2, 0, 3, 0, -4]
    expected_output = [[0, 0, 5], [1, 0, 4]]
    assert descartes(poly_array) == expected_output

def test_descartes_3():
    poly_array = [2, 0, 3, 0, 4]
    expected_output = []
    assert descartes(poly_array) == expected_output

def test_descartes_4():
    poly_array = [-2, 0, -3, 0, -4]
    expected_output = [[1, 1, 2]]
    assert descartes(poly_array) == expected_output

def test_descartes_5():
    poly_array = [0, 0, 0, 0, 0]
    expected_output = []
    assert descartes(poly_array) == expected_output

def test_descartes_6():
    poly_array = [2, 3, -4, 0, 1]
    expected_output = [[0, 0, 5], [1, 0, 4]]
    assert descartes(poly_array) == expected_output
