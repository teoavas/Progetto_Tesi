from funzione import circle_line_intersection

def test_circle_line_intersection_1():
    assert circle_line_intersection((0, 0), 5, (10, 0), (15, 0)) == [(12.5, 0)]

def test_circle_line_intersection_2():
    assert circle_line_intersection((0, 0), 5, (0, 0), (1, 1)) == []

def test_circle_line_intersection_3():
    assert circle_line_intersection((0, 0), 5, (10, 0), (15, 0), full_line=False) == [(12.5, 0)]

def test_circle_line_intersection_4():
    assert circle_line_intersection((0, 0), 5, (1, 1), (2, 2)) == []

def test_circle_line_intersection_5():
    assert circle_line_intersection((0, 0), 5, (10, 0), (15, 0), tangent_tol=1e-6) == [(12.5, 0)]

def test_circle_line_intersection_6():
    assert circle_line_intersection((-3, -4), 2, (-2, -1), (-1, 0)) == []

def test_circle_line_intersection_7():
    assert circle_line_intersection((0, 0), 5, (10, 10), (15, 20)) == [(12.5, 12.5)]
