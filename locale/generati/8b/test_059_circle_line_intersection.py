from funzione import circle_line_intersection

def test_circle_line_intersection_1():
    result = circle_line_intersection((0, 0), 5, (10, 0), (-10, 0))
    assert result == [(0.0, 0.0)]

def test_circle_line_intersection_2():
    result = circle_line_intersection((0, 0), 5, (3, 4), (-3, -4))
    assert result == []

def test_circle_line_intersection_3():
    result = circle_line_intersection((0, 0), 1, (10, 0), (-10, 0))
    assert result == [(0.0, 0.0)]

def test_circle_line_intersection_4():
    result = circle_line_intersection((0, 0), 5, (3, 4), (-3, -4), full_line=False)
    assert result == []

def test_circle_line_intersection_5():
    result = circle_line_intersection((0, 0), 1, (10, 0), (-10, 0), full_line=False)
    assert result == [(0.0, 0.0)]

def test_circle_line_intersection_6():
    result = circle_line_intersection((0, 0), 5, (3, 4), (-3, -4), tangent_tol=1e-8)
    assert result == []

def test_circle_line_intersection_7():
    result = circle_line_intersection((0, 0), 5, (10, 0), (-10, 0), full_line=False, tangent_tol=1e-8)
    assert result == []
