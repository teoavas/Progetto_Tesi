from funzione import check_dead_corner

def test_check_dead_corner_1():
    assert check_dead_corner((0, 0), []) == False

def test_check_dead_corner_2():
    assert check_dead_corner((10, 10), [(5, 5)]) == True

def test_check_dead_corner_3():
    assert check_dead_corner((0, 0), [(1, 1), (2, 2)]) == False

def test_check_dead_corner_4():
    assert check_dead_corner((10, 10), [(9, 9), (8, 8)]) == True

def test_check_dead_corner_5():
    assert check_dead_corner((0, 0), [(1, 1), (2, 2), (3, 3)]) == False

def test_check_dead_corner_6():
    assert check_dead_corner((10, 10), [(9, 9), (8, 8), (7, 7)]) == True

def test_check_dead_corner_7():
    assert check_dead_corner((-1, -1), []) == False
