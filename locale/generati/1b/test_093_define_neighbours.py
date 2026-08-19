def test_define_neighbours_1():
    assert define_neighbours([[0, 0], [0, 1]], 0, 0) == [[-1, 0], [0, 1]]
    assert define_neighbours([[0, 0], [0, 2]], 0, 0) == [[-1, 0], [-1, 1]]

def test_define_neighbours_2():
    assert define_neighbours([[0, 0], [0, 3]], 0, 0) == [[-1, 0], [-1, 1]]
    assert define_neighbours([[0, 0], [0, 4]], 0, 0) == [[-1, 0], [-1, 1]]

def test_define_neighbours_3():
    assert define_neighbours([[0, 0], [2, 0]], 0, 0) == [[-1, 0], [-1, -1]]
    assert define_neighbours([[0, 0], [4, 0]], 0, 0) == [[-1, 0], [-1, -1]]

def test_define_neighbours_4():
    assert define_neighbours([[0, 0], [6, 0]], 0, 0) == [[-1, 0], [-1, -1]]
    assert define_neighbours([[0, 0], [8, 0]], 0, 0) == [[-1, 0], [-1, -1]]

def test_define_neighbours_5():
    assert define_neighbours([[0, 0], [10, 0]], 0, 0) == [[-1, 0], [-1, -1]]
    assert define_neighbours([[0, 0], [12, 0]], 0, 0) == [[-1, 0], [-1, -1]]

def test_define_neighbours_6():
    assert define_neighbours([[0, 0], [14, 0]], 0, 0) == [[-1, 0], [-1, -1]]
    assert define_neighbours([[0, 0], [16, 0]], 0, 0) == [[-1, 0], [-1, -1]]

def test_define_neighbours_7():
    assert define_neighbours([[0, 0], [18, 0]], 0, 0) == [[-1, 0], [-1, -1]]
    assert define_neighbours([[0, 0], [20, 0]], 0, 0) == [[-1, 0], [-1, -1]]

def test_define_neighbours_8():
    assert define_neighbours([[0, 0], [22, 0]], 0, 0) == [[-1, 0], [-1, -1]]
    assert define_neighbours([[0, 0], [24, 0]], 0, 0) == [[-1, 0], [-1, -1]]
