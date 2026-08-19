from funzione import get_intersect_point

def test_get_intersect_point_1():
    v1 = [0, 0]
    v2 = [10, 10]
    width = 100
    height = 100
    assert get_intersect_point(v1, v2, width, height) == None

def test_get_intersect_point_2():
    v1 = [0, 0]
    v2 = [10, 20]
    width = 100
    height = 100
    assert get_intersect_point(v1, v2, width, height) == [0, round(5)]

def test_get_intersect_point_3():
    v1 = [0, 0]
    v2 = [10, -20]
    width = 100
    height = 100
    assert get_intersect_point(v1, v2, width, height) == None

def test_get_intersect_point_4():
    v1 = [0, 0]
    v2 = [-10, 20]
    width = 100
    height = 100
    assert get_intersect_point(v1, v2, width, height) == [round(-5), 0]

def test_get_intersect_point_5():
    v1 = [0, 0]
    v2 = [10, -20]
    width = 50
    height = 50
    assert get_intersect_point(v1, v2, width, height) == None

def test_get_intersect_point_6():
    v1 = [0, 0]
    v2 = [-10, 20]
    width = 100
    height = 200
    assert get_intersect_point(v1, v2, width, height) == [round(-5), 0]

def test_get_intersect_point_7():
    v1 = [0, 0]
    v2 = [10, -20]
    width = 50
    height = 100
    assert get_intersect_point(v1, v2, width, height) == None

def test_get_intersect_point_8():
    v1 = [0, 0]
    v2 = [-10, 20]
    width = 200
    height = 100
    assert get_intersect_point(v1, v2, width, height) == [round(-5), 0]
