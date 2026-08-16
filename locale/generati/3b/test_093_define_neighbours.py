from funzione import define_neighbours

def test_define_neighbours_1():
    assert len(define_neighbours([[0, 0], [0, 0]], 0, 0)) == 6

def test_define_neighbours_2():
    assert define_neighbours([[0, 0], [0, 0]], 0, 1) == [[-1, 1], [-1, 0], [0, 1]]

def test_define_neighbours_3():
    assert len(define_neighbours([[0, 0], [0, 0]], 1, 1)) == 6

def test_define_neighbours_4():
    assert define_neighbours([[0, 0], [0, 0]], 0, 2) == [[-1, 2], [-1, 1], [0, 2]]

def test_define_neighbours_5():
    assert len(define_neighbours([[0, 0], [0, 0]], 2, 2)) == 6

def test_define_neighbours_6():
    assert define_neighbours([[0, 0], [0, 0]], 1, 0) == [[-1, 0], [-1, -1]]

def test_define_neighbours_7():
    assert len(define_neighbours([[0, 0], [0, 0]], 2, 0)) == 6
