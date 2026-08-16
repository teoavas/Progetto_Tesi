```python
from funzione import get_text_point_at_line

def test_get_text_point_at_line_1():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (100, 200)
    align = 'center'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (50.0, -15.0)

def test_get_text_point_at_line_2():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (100, 200)
    align = 'left'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (5.0, -15.0)

def test_get_text_point_at_line_3():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'center'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-55.0, -15.0)

def test_get_text_point_at_line_4():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'left'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-60.0, -15.0)

def test_get_text_point_at_line_5():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'right'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-50.0, -15.0)

def test_get_text_point_at_line_6():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'top'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-55.0, -25.0)

def test_get_text_point_at_line_7():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'bottom'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-55.0, -15.0)

def test_get_text_point_at_line_8():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'center'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-55.0, -15.0)

def test_get_text_point_at_line_9():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'left'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-60.0, -15.0)

def test_get_text_point_at_line_10():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'right'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-50.0, -15.0)

def test_get_text_point_at_line_11():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'top'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-55.0, -25.0)

def test_get_text_point_at_line_12():
    extents = (10, 20)
    p1 = (100, 200)
    p2 = (0, 0)
    align = 'bottom'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-55.0, -15.0)

def test_get_text_point_at_line_13():
    extents = (10, 20)
    p1 = (100,
