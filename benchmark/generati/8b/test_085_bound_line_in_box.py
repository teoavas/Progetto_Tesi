from funzione import bound_line_in_box

def test_bound_line_in_box_1():
    assert bound_line_in_box(10, 10, 5, 5, 1, 1, 0) == (True, 5, 5)

def test_bound_line_in_box_2():
    assert bound_line_in_box(10, 10, 5, 5, 1, 1, 1) == (True, 5, 5)

def test_bound_line_in_box_3():
    assert bound_line_in_box(10, 10, 5, 5, 1, 1, -1) == (False, 6.0, 6.0)

def test_bound_line_in_box_4():
    assert bound_line_in_box(10, 10, 5, 5, 1, 1, 2) == (False, 7.0710678118654755, 7.0710678118654755)

def test_bound_line_in_box_5():
    assert bound_line_in_box(10, 10, 5, 5, 1, 1, 10) == (None, -5, -5)

def test_bound_line_in_box_6():
    assert bound_line_in_box(10, 10, 5, 5, 1, 1, -10) == (None, -5, -5)

def test_bound_line_in_box_7():
    assert bound_line_in_box(10, 10, 0, 0, 1, 1, 0) == (True, 0, 0)

def test_bound_line_in_box_8():
    assert bound_line_in_box(10, 10, 10, 10, 1, 1, 0) == (None, -10, -10)
