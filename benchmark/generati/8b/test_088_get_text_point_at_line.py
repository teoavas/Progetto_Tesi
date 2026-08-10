from funzione import get_text_point_at_line

def test_get_text_point_at_line_1():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (10, 20)
    align = 'left'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (5, -25)

def test_get_text_point_at_line_2():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (10, 20)
    align = 'right'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-15, -25)

def test_get_text_point_at_line_3():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (10, 20)
    align = 'center'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-5, -25)

def test_get_text_point_at_line_4():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (10, 20)
    align = 'left'
    padding = 0
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (5, -25)

def test_get_text_point_at_line_5():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (10, 20)
    align = 'right'
    padding = 0
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-15, -25)

def test_get_text_point_at_line_6():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (10, 20)
    align = 'center'
    padding = 0
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-5, -25)

def test_get_text_point_at_line_7():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (10, 20)
    align = 'left'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (5, -25)

def test_get_text_point_at_line_8():
    extents = (10, 20)
    p1 = (0, 0)
    p2 = (10, 20)
    align = 'right'
    padding = 5
    assert get_text_point_at_line(extents, p1, p2, align, padding) == (-15, -25)
