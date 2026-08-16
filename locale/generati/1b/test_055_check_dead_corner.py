import pytest

def test_check_dead_corner_1():
    assert check_dead_corner((0, 0), [(1, 2), (3, 4)])
    assert check_dead_corner((5, 6), [(7, 8), (9, 10)])

def test_check_dead_corner_2():
    assert not check_dead_corner((-1, -1), [(1, 2), (3, 4)])

def test_check_dead_corner_3():
    assert check_dead_corner((0, 0), [])

def test_check_dead_corner_4():
    assert check_dead_corner((10, 20), [(5, 6), (7, 8)])

def test_check_dead_corner_5():
    assert not check_dead_corner((-1, -1), [(3, 4), (5, 6)])

def test_check_dead_corner_6():
    assert check_dead_corner((0, 0), [(10, 20)])
