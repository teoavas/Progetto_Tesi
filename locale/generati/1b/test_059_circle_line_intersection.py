import pytest
from funzione import circle_line_intersection

def test_circle_line_intersection_1():
    assert circle_line_intersection((0, 0), 5, (2, 3), (4, 6)) == [(2.23606797749979, 3.23606797749979)]

def test_circle_line_intersection_2():
    assert circle_line_intersection((0, 0), 5, (-1, -1), (1, 1)) == []

def test_circle_line_intersection_3():
    assert circle_line_intersection((0, 0), 5, (6, 4), (8, 2)) == [(4.23606797749979, 2.23606797749979)]

def test_circle_line_intersection_4():
    assert circle_line_intersection((0, 0), 5, (-1, -3), (1, 1)) == []

def test_circle_line_intersection_5():
    assert circle_line_intersection((0, 0), 5, (2, 6), (8, 2)) == [(4.23606797749979, 2.23606797749979)]

def test_circle_line_intersection_6():
    assert circle_line_intersection((0, 0), 5, (-1, -3), (9, 7)) == []

def test_circle_line_intersection_7():
    assert circle_line_intersection((0, 0), 5, (2, 4), (8, 12)) == [(6.23606797749979, 8.23606797749979)]

def test_circle_line_intersection_8():
    assert circle_line_intersection((0, 0), 5, (-1, -3), (9, 7), full_line=False) == []
