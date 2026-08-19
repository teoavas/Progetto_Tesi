from funzione import get_text_point_at_line

def test_get_text_point_at_line_1():
    assert get_text_point_at_line((100, 200), (0, 0), (10, 10), 'left', 5) == (5.0, 5.0)

def test_get_text_point_at_line_2():
    assert get_text_point_at_line((100, 200), (0, 0), (10, 10), 'right', 5) == (15.0, 5.0)

def test_get_text_point_at_line_3():
    assert get_text_point_at_line((100, 200), (0, 0), (10, 10), 'center', 5) == (7.5, 5.0)

def test_get_text_point_at_line_4():
    assert get_text_point_at_line((100, 200), (0, 0), (10, 10), 'bottom', 5) == (5.0, 15.0)

def test_get_text_point_at_line_5():
    assert get_text_point_at_line((100, 200), (0, 0), (10, 10), 'top', 5) == (5.0, -5.0)

def test_get_text_point_at_line_6():
    assert get_text_point_at_line((100, 200), (0, 0), (10, 10), 'left', 0) == (0.0, 5.0)

def test_get_text_point_at_line_7():
    assert get_text_point_at_line((100, 200), (0, 0), (10, 10), 'right', 0) == (10.0, 5.0)

def test_get_text_point_at_line_8():
    assert get_text_point_at_line((100, 200), (0, 0), (10, 10), 'center', 0) == (5.0, 5.0)
