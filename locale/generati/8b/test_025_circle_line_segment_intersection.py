from funzione import circle_line_segment_intersection

def test_circle_line_segment_intersection_1():
    result = circle_line_segment_intersection((0, 0), 5, (10, 0), (-10, 0))
    assert len(result) == 2

def test_circle_line_segment_intersection_2():
    result = circle_line_segment_intersection((0, 0), 5, (10, 0), (-10, 0), full_line=False)
    assert len(result) == 1

def test_circle_line_segment_intersection_3():
    result = circle_line_segment_intersection((0, 0), 5, (0, 0), (0, 0))
    assert len(result) == []

def test_circle_line_segment_intersection_4():
    result = circle_line_segment_intersection((0, 0), 1e-9, (10, 0), (-10, 0))
    assert len(result) == 2

def test_circle_line_segment_intersection_5():
    result = circle_line_segment_intersection((0, 0), 5, (10, 10), (20, -20))
    assert len(result) == []

def test_circle_line_segment_intersection_6():
    result = circle_line_segment_intersection((0, 0), 1e-9, (10, 10), (20, -20))
    assert len(result) == 2

def test_circle_line_segment_intersection_7():
    result = circle_line_segment_intersection((0, 0), 5, (10, 10), (20, -20), full_line=False)
    assert len(result) == 1
