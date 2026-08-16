import pytest
from funzione import circle_line_segment_intersection

def test_circle_line_segment_intersection_1():
    assert circle_line_segment_intersection((0, 0), 5, (2, 3), (4, 6)) == [(2.23606797749979, 3.23606797749979)]

def test_circle_line_segment_intersection_2():
    assert circle_line_segment_intersection((0, 0), 5, (-2, -3), (4, 6)) == []

def test_circle_line_segment_intersection_3():
    assert circle_line_segment_intersection((0, 0), 5, (1, 1), (3, 3)) == [(1.23606797749979, 1.23606797749979)]

def test_circle_line_segment_intersection_4():
    assert circle_line_segment_intersection((0, 0), 5, (-2, -3), (6, 6)) == []

def test_circle_line_segment_intersection_5():
    assert circle_line_segment_intersection((0, 0), 5, (1.23606797749979, 1.23606797749979)) == [(1.23606797749979, 1.23606797749979)]

def test_circle_line_segment_intersection_6():
    assert circle_line_segment_intersection((0, 0), 5, (-2, -3), (4, 4)) == []

def test_circle_line_segment_intersection_7():
    assert circle_line_segment_intersection((0, 0), 5, (1.23606797749979, 1.23606797749979), (6, 6)) == [(1.23606797749979, 1.23606797749979)]

def test_circle_line_segment_intersection_8():
    assert circle_line_segment_intersection((0, 0), 5, (-2, -3), (4, 4), tangent_tol=1e-9) == [(1.23606797749979, 1.23606797749979)]
