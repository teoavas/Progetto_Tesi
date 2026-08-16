from funzione import bound_line_in_box

def test_bound_line_in_box_1():
    w, h = 10.0, 20.0
    x0, y0 = 5.0, 15.0
    dir_x, dir_y = 2.0, 3.0
    length_margin = 1.0
    result, bound_x, bound_y = bound_line_in_box(w, h, x0, y0, dir_x, dir_y, length_margin)
    assert result is True

def test_bound_line_in_box_2():
    w, h = 10.0, 20.0
    x0, y0 = 5.0, 15.0
    dir_x, dir_y = -2.0, 3.0
    length_margin = -1.0
    result, bound_x, bound_y = bound_line_in_box(w, h, x0, y0, dir_x, dir_y, length_margin)
    assert result is False

def test_bound_line_in_box_3():
    w, h = 10.0, 20.0
    x0, y0 = 5.0, 15.0
    dir_x, dir_y = 2.0, -3.0
    length_margin = 1.0
    result, bound_x, bound_y = bound_line_in_box(w, h, x0, y0, dir_x, dir_y, length_margin)
    assert result is True

def test_bound_line_in_box_4():
    w, h = 10.0, 20.0
    x0, y0 = 5.0, 15.0
    dir_x, dir_y = -2.0, -3.0
    length_margin = -1.0
    result, bound_x, bound_y = bound_line_in_box(w, h, x0, y0, dir_x, dir_y, length_margin)
    assert result is False

def test_bound_line_in_box_5():
    w, h = 10.0, 20.0
    x0, y0 = 5.0, 15.0
    dir_x, dir_y = 2.0, 3.0
    length_margin = -1.0
    result, bound_x, bound_y = bound_line_in_box(w, h, x0, y0, dir_x, dir_y, length_margin)
    assert result is None

def test_bound_line_in_box_6():
    w, h = 10.0, 20.0
    x0, y0 = 5.0, 15.0
    dir_x, dir_y = -2.0, 3.0
    length_margin = 1.0
    result, bound_x, bound_y = bound_line_in_box(w, h, x0, y0, dir_x, dir_y, length_margin)
    assert math.isclose(bound_x, 10.0)

def test_bound_line_in_box_7():
    w, h = 10.0, 20.0
    x0, y0 = 5.0, 15.0
    dir_x, dir_y = -2.0, 3.0
    length_margin = 1.0
    result, bound_x, bound_y = bound_line_in_box(w, h, x0, y0, dir_x, dir_y, length_margin)
    assert math.isclose(bound_y, 19.5)

def test_bound_line_in_box_8():
    w, h = 10.0, 20.0
    x0, y0 = 5.0, 15.0
    dir_x, dir_y = -2.0, 3.0
    length_margin = 1.0
    result, bound_x, bound_y = bound_line_in_box(w, h, x0, y0, dir_x, dir_y, length_margin)
    assert math.isclose(bound_dist, 4.123105625617661)
