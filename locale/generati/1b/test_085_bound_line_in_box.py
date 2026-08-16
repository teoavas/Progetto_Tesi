import pytest
from funzione import bound_line_in_box

def test_bound_line_in_box_1():
    assert bound_line_in_box(0.5, 2.0, 1.0, 1.0, 1.0, 0.0) == (None, -1.0, -1.0)

def test_bound_line_in_box_2():
    assert bound_line_in_box(-1.0, 3.0, 4.0, 5.0, -1.0, 0.0) == (None, -4.0, -5.0)

def test_bound_line_in_box_3():
    assert bound_line_in_box(2.0, 1.0, 6.0, 7.0, 1.0, 0.0) == (None, -6.0, -7.0)

def test_bound_line_in_box_4():
    assert bound_line_in_box(-3.0, 8.0, 9.0, 10.0, -2.0, 0.0) == (None, -9.0, -10.0)

def test_bound_line_in_box_5():
    assert bound_line_in_box(1.0, 4.0, 3.0, 6.0, 1.0, 0.0) == (None, -2.0, -3.0)

def test_bound_line_in_box_6():
    assert bound_line_in_box(-5.0, 9.0, 10.0, 11.0, -4.0, 0.0) == (None, -11.0, -12.0)

def test_bound_line_in_box_7():
    assert bound_line_in_box(2.0, 1.0, 6.0, 7.0, 1.0, 0.0) == (None, -6.0, -7.0)
