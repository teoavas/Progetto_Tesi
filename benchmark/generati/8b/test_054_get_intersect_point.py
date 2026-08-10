from funzione import get_intersect_point

def test_get_intersect_point_1():
    assert get_intersect_point([0, 0], [0, 10], 10, 10) == [0, 0]

def test_get_intersect_point_2():
    assert get_intersect_point([0, 0], [10, 0], 10, 10) == [0, 0]

def test_get_intersect_point_3():
    assert get_intersect_point([0, 0], [10, 10], 10, 10) == [5, 5]

def test_get_intersect_point_4():
    assert get_intersect_point([0, 0], [10, 10], 10, 5) == [5, 5]

def test_get_intersect_point_5():
    assert get_intersect_point([0, 0], [10, 10], 5, 10) == [5, 5]

def test_get_intersect_point_6():
    assert get_intersect_point([0, 0], [10, 10], 0, 10) == [0, 0]

def test_get_intersect_point_7():
    assert get_intersect_point([0, 0], [10, 10], 10, 0) == [0, 0]

def test_get_intersect_point_8():
    assert get_intersect_point([0, 0], [10, 10], 10, 10) == [5, 5]
