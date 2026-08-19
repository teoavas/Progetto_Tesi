import pytest

def test___transform_coors_1():
    assert __transform_coors((0, 0), 0, 0, 10, 10) == (5, 5, 15, 15)

def test___transform_coors_2():
    assert __transform_coors((20, 20), 0, 0, 10, 10) == (25, 25, 35, 35)

def test___transform_coors_3():
    assert __transform_coors((40, 40), 1, 1, 5, 5) == (45, 45, 55, 55)

def test___transform_coors_4():
    assert __transform_coors((60, 60), 2, 2, 10, 10) == (65, 65, 75, 75)

def test___transform_coors_5():
    assert __transform_coors((80, 80), 3, 3, 15, 15) == (85, 85, 95, 95)

def test___transform_coors_6():
    assert __transform_coors((100, 100), 4, 4, 20, 20) == (105, 105, 115, 115)

def test___transform_coors_7():
    assert __transform_coors((120, 120), 5, 5, 25, 25) == (125, 125, 135, 135)

def test___transform_coors_8():
    assert __transform_coors((140, 140), 6, 6, 30, 30) == (145, 145, 155, 155)
