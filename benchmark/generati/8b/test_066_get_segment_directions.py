from funzione import get_segment_directions

def test_get_segment_directions_1():
    matrix_dimensions = [10, 10]
    assert get_segment_directions(5, 5, 2, matrix_dimensions) == ['N', 'E', 'S', 'W']

def test_get_segment_directions_2():
    matrix_dimensions = [10, 10]
    assert get_segment_directions(0, 0, 2, matrix_dimensions) == ['N', 'E', 'S', 'W']

def test_get_segment_directions_3():
    matrix_dimensions = [10, 10]
    assert get_segment_directions(5, 5, 1, matrix_dimensions) == ['N', 'E', 'S', 'W']

def test_get_segment_directions_4():
    matrix_dimensions = [10, 10]
    assert get_segment_directions(5, 5, 3, matrix_dimensions) == ['N', 'E', 'S', 'W', 'NW', 'NE', 'SW', 'SE']

def test_get_segment_directions_5():
    matrix_dimensions = [10, 10]
    try:
        get_segment_directions(-1, 5, 2, matrix_dimensions)
        assert False, "Expected an exception"
    except Exception as e:
        assert str(e) == "The point (-1, 5) doesn't belong into the matrix"

def test_get_segment_directions_6():
    matrix_dimensions = [10, 10]
    try:
        get_segment_directions(5, -1, 2, matrix_dimensions)
        assert False, "Expected an exception"
    except Exception as e:
        assert str(e) == "The point (5, -1) doesn't belong into the matrix"

def test_get_segment_directions_7():
    matrix_dimensions = [10, 10]
    try:
        get_segment_directions(11, 5, 2, matrix_dimensions)
        assert False, "Expected an exception"
    except Exception as e:
        assert str(e) == "The point (11, 5) doesn't belong into the matrix"

def test_get_segment_directions_8():
    matrix_dimensions = [10, 10]
    try:
        get_segment_directions(5, 11, 2, matrix_dimensions)
        assert False, "Expected an exception"
    except Exception as e:
        assert str(e) == "The point (5, 11) doesn't belong into the matrix"
