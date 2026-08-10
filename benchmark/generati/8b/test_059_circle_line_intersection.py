from funzione import circle_line_intersection

def test_circle_line_intersection_1():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 5)
    pt2 = (0, -5)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == [(0, 0)]

def test_circle_line_intersection_2():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 5)
    pt2 = (0, 10)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == [(0, 5)]

def test_circle_line_intersection_3():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 5)
    pt2 = (0, -5)
    full_line = False
    tangent_tol = 1e-9
    assert circle_line_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == [(0, 0)]

def test_circle_line_intersection_4():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 5)
    pt2 = (0, -5)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == [(0, 0)]

def test_circle_line_intersection_5():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 5)
    pt2 = (0, -5)
    full_line = True
    tangent_tol = 1e-8
    assert circle_line_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == []

def test_circle_line_intersection_6():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 5)
    pt2 = (0, -5)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == [(0, 0)]

def test_circle_line_intersection_7():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 5)
    pt2 = (0, -5)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == [(0, 0)]

def test_circle_line_intersection_8():
    circle_center = (0, 0)
    circle_radius = 5
    pt1 = (0, 5)
    pt2 = (0, -5)
    full_line = True
    tangent_tol = 1e-9
    assert circle_line_intersection(circle_center, circle_radius, pt1, pt2, full_line, tangent_tol) == [(0, 0)]
