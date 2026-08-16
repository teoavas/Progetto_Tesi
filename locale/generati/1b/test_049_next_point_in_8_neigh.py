import pytest

def test_next_point_in_8_neigh_1():
    assert next_point_in_8_neigh((0, 0), (1, 0)) == (0, -1)

def test_next_point_in_8_neigh_2():
    assert next_point_in_8_neigh((0, 0), (0, 1)) == (-1, 0)

def test_next_point_in_8_neigh_3():
    assert next_point_in_8_neigh((0, 0), (1, 1)) == (0, -2)

def test_next_point_in_8_neigh_4():
    assert next_point_in_8_neigh((0, 0), (0, 2)) == (-2, 0)

def test_next_point_in_8_neigh_5():
    assert next_point_in_8_neigh((0, 0), (1, 3)) == (0, -3)

def test_next_point_in_8_neigh_6():
    assert next_point_in_8_neigh((0, 0), (2, 4)) == (-3, 0)

def test_next_point_in_8_neigh_7():
    assert next_point_in_8_neigh((0, 0), (1, 5)) == (0, -5)

def test_next_point_in_8_neigh_8():
    assert next_point_in_8_neigh((0, 0), (2, 6)) == (-5, 0)
