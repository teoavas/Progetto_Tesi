from funzione import define_neighbours

def test_define_neighbours_1():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 1
    j = 1
    assert define_neighbours(matrix, i, j) == [[0, 1], [0, 2], [2, 1], [2, 2], [3, 1], [3, 2], [1, 2], [1, 0]]

def test_define_neighbours_2():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 0
    j = 1
    assert define_neighbours(matrix, i, j) == [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]]

def test_define_neighbours_3():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 2
    j = 1
    assert define_neighbours(matrix, i, j) == [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]]

def test_define_neighbours_4():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 1
    j = 0
    assert define_neighbours(matrix, i, j) == [[0, 2], [0, 3], [2, 3], [3, 3], [4, 3], [5, 3]]

def test_define_neighbours_5():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 1
    j = 2
    assert define_neighbours(matrix, i, j) == [[0, 1], [0, 3], [2, 1], [2, 3]]

def test_define_neighbours_6():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 1
    j = 1
    assert define_neighbours(matrix, i, j) == [[0, 1], [0, 2], [2, 1], [2, 2], [3, 1], [3, 2], [1, 2], [1, 0]]

def test_define_neighbours_7():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 0
    j = 2
    assert define_neighbours(matrix, i, j) == [[1, 2], [3, 2], [4, 2], [5, 2], [6, 2]]

def test_define_neighbours_8():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 1
    j = 1
    assert define_neighbours(matrix, i, j) == [[0, 1], [0, 2], [2, 1], [2, 2], [3, 1], [3, 2], [1, 2], [1, 0]]
