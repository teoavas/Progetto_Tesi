from funzione import check_dead_corner

def test_check_dead_corner_1():
    xanadu = [10, 20]
    other_objs = [[5, 15], [12, 22]]
    assert check_dead_corner(xanadu, other_objs) == True

def test_check_dead_corner_2():
    xanadu = [10, 20]
    other_objs = [[11, 21], [12, 22]]
    assert check_dead_corner(xanadu, other_objs) == False

def test_check_dead_corner_3():
    xanadu = [10, 20]
    other_objs = [[5, 15], [25, 35]]
    assert check_dead_corner(xanadu, other_objs) == True

def test_check_dead_corner_4():
    xanadu = [10, 20]
    other_objs = [[11, 21], [12, 22], [13, 23]]
    assert check_dead_corner(xanadu, other_objs) == False

def test_check_dead_corner_5():
    xanadu = [10, 20]
    other_objs = []
    assert check_dead_corner(xanadu, other_objs) == True

def test_check_dead_corner_6():
    xanadu = [10, 20]
    other_objs = [[11, 21], [12, 22], [13, 23]]
    assert check_dead_corner(xanadu, other_objs) == False
