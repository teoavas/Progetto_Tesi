import pytest

def test_is_degree_in_degree_range_1():
    assert is_degree_in_degree_range(0, 90, 180) == True

def test_is_degree_in_degree_range_2():
    assert is_degree_in_degree_range(-90, -30, 60) == False

def test_is_degree_in_degree_range_3():
    assert is_degree_in_degree_range(150, 120, 90) == True

def test_is_degree_in_degree_range_4():
    assert is_degree_in_degree_range(-180, -45, 135) == False

def test_is_degree_in_degree_range_5():
    assert is_degree_in_degree_range(0, 0, 0) == True

def test_is_degree_in_degree_range_6():
    assert is_degree_in_degree_range(90, 120, 150) == False
