from funzione import __transform_coors

def test___transform_coors_1():
    assert __transform_coors((0, 0, 10, 10), 2, 3, 5, 7) == (0, 0, 5, 7)

def test___transform_coors_2():
    assert __transform_coors((10, 10, 20, 20), 4, 6, 8, 10) == (10, 10, 16, 18)

def test___transform_coors_3():
    assert __transform_coors((-5, -5, 0, 0), 2, 3, 5, 7) == (-5, -5, 0, 0)

def test___transform_coors_4():
    assert __transform_coors((10, 10, 20, 20), 1, 1, 5, 7) == (10, 10, 15, 17)

def test___transform_coors_5():
    assert __transform_coors((-10, -10, 0, 0), 2, 3, 5, 7) == (-10, -10, 0, 0)

def test___transform_coors_6():
    assert __transform_coors((0, 0, 10, 10), 1, 1, 5, 7) == (0, 0, 5, 7)

def test___transform_coors_7():
    assert __transform_coors((-5, -5, 20, 20), 2, 3, 5, 7) == (-5, -5, 15, 17)
