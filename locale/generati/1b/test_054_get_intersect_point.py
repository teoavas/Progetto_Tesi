import pytest

def test_get_intersect_point_1():
    assert get_intersect_point([0, 0], [10, 10], 100, 100) == [50, 25]

def test_get_intersect_point_2():
    assert get_intersect_point([5, 5], [15, 15], 200, 200) == [150, 75]

def test_get_intersect_point_3():
    assert get_intersect_point([0, 0], [10, 10], 50, 50) is None

def test_get_intersect_point_4():
    assert get_intersect_point([5, 5], [15, 15], 300, 300) == [225, 125]

def test_get_intersect_point_5():
    assert get_intersect_point([-1, -1], [-10, -10], 400, 400) is None

def test_get_intersect_point_6():
    assert get_intersect_point([0, 0], [100, 100], 200, 200) == [50, 25]

def test_get_intersect_point_7():
    assert get_intersect_point([-5, -5], [-15, -15], 250, 250) is None

def test_get_intersect_point_8():
    assert get_intersect_point([0, 0], [100, 100], 150, 150) == [75, 37]
