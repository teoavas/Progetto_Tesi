from funzione import check_dead_corner

def test_check_dead_corner_1():
    xanadu = [0, 0]
    other_objs = [[1, 1], [2, 2]]
    assert check_dead_corner(xanadu, other_objs) == True

def test_check_dead_corner_2():
    xanadu = [0, 0]
    other_objs = [[-1, -1], [2, 2]]
    assert check_dead_corner(xanadu, other_objs) == True

def test_check_dead_corner_3():
    xanadu = [0, 0]
    other_objs = [[1, 1], [-2, -2]]
    assert check_dead_corner(xanadu, other_objs) == True

def test_check_dead_corner_4():
    xanadu = [0, 0]
    other_objs = [[1, 1], [2, 2]]
    assert check_dead_corner(xanadu, other_objs) == False

def test_check_dead_corner_5():
    xanadu = [0, 0]
    other_objs = [[-1, -1], [-2, -2]]
    assert check_dead_corner(xanadu, other_objs) == False

def test_check_dead_corner_6():
    xanadu = [0, 0]
    other_objs = [[1, 1], [1, 1]]
    assert check_dead_corner(xanadu, other_objs) == False

def test_check_dead_corner_7():
    xanadu = [0, 0]
    other_objs = [[-1, -1], [-1, -1]]
    assert check_dead_corner(xanadu, other_objs) == False
