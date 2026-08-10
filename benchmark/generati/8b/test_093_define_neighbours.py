from funzione import define_neighbours

def test_define_neighbours_1():
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 1
    j = 1
    assert define_neighbours(m, i, j) == [[0, 0], [0, 2], [0, 0], [2, 2], [0, 2], [2, 0], [0, 0], [0, 0]]

def test_define_neighbours_2():
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 0
    j = 1
    assert define_neighbours(m, i, j) == [[1, 1], [2, 1], [0, 2], [2, 2], [2, 1], [2, 0], [0, 2], [2, 0]]

def test_define_neighbours_3():
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 2
    j = 1
    assert define_neighbours(m, i, j) == [[1, 1], [2, 1], [0, 1], [2, 2], [1, 2], [2, 0], [0, 1], [1, 0]]

def test_define_neighbours_4():
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 1
    j = 0
    assert define_neighbours(m, i, j) == [[0, 0], [0, 2], [0, 0], [2, 2], [0, 2], [2, 0], [0, 0], [0, 0]]

def test_define_neighbours_5():
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 1
    j = 2
    assert define_neighbours(m, i, j) == [[0, 0], [0, 2], [0, 0], [2, 2], [0, 2], [2, 0], [0, 0], [0, 0]]

def test_define_neighbours_6():
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 0
    j = 2
    assert define_neighbours(m, i, j) == [[1, 1], [2, 1], [0, 2], [2, 2], [2, 1], [2, 0], [0, 2], [2, 0]]

def test_define_neighbours_7():
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 2
    j = 2
    assert define_neighbours(m, i, j) == [[1, 1], [2, 1], [0, 1], [2, 2], [1, 2], [2, 0], [0, 1], [1, 0]]
