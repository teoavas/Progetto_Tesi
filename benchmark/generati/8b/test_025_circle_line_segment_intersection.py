from funzione import circle_line_segment_intersection
import math

def test_circle_line_segment_intersection_1():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (0, 10)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []

def test_circle_line_segment_intersection_2():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (10, 0)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == [(5, 0)]

def test_circle_line_segment_intersection_3():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (10, 10)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []

def test_circle_line_segment_intersection_4():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (10, 10)
    full_line = False
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []

def test_circle_line_segment_intersection_5():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (10, 10)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []

def test_circle_line_segment_intersection_6():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (10, 10)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []

def test_circle_line_segment_intersection_7():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (10, 10)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []

def test_circle_line_segment_intersection_8():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (10, 10)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []

def test_circle_line_segment_intersection_9():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (10, 10)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []

def test_circle_line_segment_intersection_10():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 0)
    pt2 = (10, 10)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []
