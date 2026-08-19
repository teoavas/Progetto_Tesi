from funzione import __transform_coors

def test___transform_coors_1():
    coor = (10, 20, 30, 40)
    i = 5
    j = 6
    xstride = 2
    ystride = 3
    assert __transform_coors(coor, i, j, xstride, ystride) == (0, 0, 2, 3)

def test___transform_coors_2():
    coor = (10, 20, 30, 40)
    i = 5
    j = 6
    xstride = 2
    ystride = 3
    assert __transform_coors(coor, i, j, xstride, ystride) == (0, 0, 2, 3)

def test___transform_coors_3():
    coor = (10, 20, 30, 40)
    i = 5
    j = 6
    xstride = 1
    ystride = 1
    assert __transform_coors(coor, i, j, xstride, ystride) == (0, 0, 1, 1)

def test___transform_coors_4():
    coor = (10, 20, 30, 40)
    i = 5
    j = 6
    xstride = 2
    ystride = 3
    assert __transform_coors(coor, i, j, xstride, ystride) == (0, 0, 2, 3)

def test___transform_coors_5():
    coor = (10, 20, 30, 40)
    i = 6
    j = 7
    xstride = 2
    ystride = 3
    assert __transform_coors(coor, i, j, xstride, ystride) == (0, 0, 4, 9)

def test___transform_coors_6():
    coor = (10, 20, 30, 40)
    i = 5
    j = 7
    xstride = 2
    ystride = 3
    assert __transform_coors(coor, i, j, xstride, ystride) == (0, 0, 4, 9)

def test___transform_coors_7():
    coor = (10, 20, 30, 40)
    i = 5
    j = 6
    xstride = 2
    ystride = 3
    assert __transform_coors(coor, i, j, xstride, ystride) == (0, 0, 2, 3)

def test___transform_coors_8():
    coor = (10, 20, 30, 40)
    i = 5
    j = 6
    xstride = 1
    ystride = 1
    assert __transform_coors(coor, i, j, xstride, ystride) == (0, 0, 1, 1)
