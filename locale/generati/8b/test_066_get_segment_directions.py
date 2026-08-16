from funzione import get_segment_directions

def test_get_segment_directions_1():
    matrix_dimensions = [10, 10]
    result = get_segment_directions(5, 5, 2, matrix_dimensions)
    assert result == ['N', 'E', 'S', 'W']

def test_get_segment_directions_2():
    matrix_dimensions = [10, 10]
    result = get_segment_directions(-1, -1, 2, matrix_dimensions)
    assert result == []

def test_get_segment_directions_3():
    matrix_dimensions = [10, 10]
    result = get_segment_directions(0, 0, 2, matrix_dimensions)
    assert result == ['N', 'E', 'S', 'W']

def test_get_segment_directions_4():
    matrix_dimensions = [10, 10]
    result = get_segment_directions(9, 9, 2, matrix_dimensions)
    assert result == ['N', 'E', 'S', 'W']

def test_get_segment_directions_5():
    matrix_dimensions = [10, 10]
    result = get_segment_directions(0, 1, 2, matrix_dimensions)
    assert result == ['E', 'S', 'W']

def test_get_segment_directions_6():
    matrix_dimensions = [10, 10]
    result = get_segment_directions(9, 8, 2, matrix_dimensions)
    assert result == ['N', 'E', 'S', 'W']

def test_get_segment_directions_7():
    matrix_dimensions = [10, 10]
    result = get_segment_directions(5, -1, 2, matrix_dimensions)
    assert result == []

def test_get_segment_directions_8():
    matrix_dimensions = [10, 10]
    result = get_segment_directions(-1, 5, 2, matrix_dimensions)
    assert result == []
