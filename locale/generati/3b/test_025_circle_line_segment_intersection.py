from funzione import circle_line_segment_intersection

def test_circle_line_segment_intersection_1():
    assert len(circle_line_segment_intersection((0, 0), 5, (10, 0), (15, 0))) == 2

def test_circle_line_segment_intersection_2():
    assert circle_line_segment_intersection((0, 0), 5, (10, 0), (15, 0)) in [(10.0, 0.0), (14.666666666666668, 0.0)]

def test_circle_line_segment_intersection_3():
    assert len(circle_line_segment_intersection((-1, -1), 2, (-1, -1), (-1, -1))) == 0

def test_circle_line_segment_intersection_4():
    assert circle_line_segment_intersection((0, 0), 5, (10, 0), (15, 0), full_line=False) in [(10.0, 0.0)]

def test_circle_line_segment_intersection_5():
    assert len(circle_line_segment_intersection((-1, -1), 2, (-1, -1), (-1, -1), full_line=False)) == 0

def test_circle_line_segment_intersection_6():
    result = circle_line_segment_intersection((0, 0), 5, (10, 0), (15, 0))
    assert len(result) > 0 and len(result) <= 2

def test_circle_line_segment_intersection_7():
    result = circle_line_segment_intersection((-1, -1), 2, (-1, -1), (-1, -1))
    assert len(result) == 0
