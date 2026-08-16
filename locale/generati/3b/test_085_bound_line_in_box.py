from funzione import bound_line_in_box

def test_bound_line_in_box_1():
    assert bound_line_in_box(10, 20, 5, 15, 2, 3, -0.5) == (False, 4.25, 16.75)

def test_bound_line_in_box_2():
    assert bound_line_in_box(10, 20, 0, 0, 1, 1, 0.5) == (True, 5.0, 5.0)

def test_bound_line_in_box_3():
    assert bound_line_in_box(10, 20, 10, 15, -2, -3, 0.5) == (False, 9.5, 12.75)

def test_bound_line_in_box_4():
    assert bound_line_in_box(10, 20, 5, 25, 2, 3, 1.0) == (True, 7.0, 22.0)

def test_bound_line_in_box_5():
    with pytest.raises(AssertionError):
        bound_line_in_box(10, 20, -1, 15, 2, 3, -0.5)

def test_bound_line_in_box_6():
    assert bound_line_in_box(10, 20, 5, 15, 2, 3, 0) == (True, 5.0, 15.0)

def test_bound_line_in_box_7():
    result = bound_line_in_box(10, 20, 5, 15, 2, 3, -1.0)
    assert result[0] is None
    assert result[1] == -5
    assert result[2] == -15
