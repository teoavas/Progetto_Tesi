from funzione import get_segment_directions

def test_get_segment_directions_1():
    assert get_segment_directions(0, 0, 2, (10, 10)) == ['N', 'W']

def test_get_segment_directions_2():
    assert get_segment_directions(5, 5, 3, (10, 10)) == ['NW', 'NE', 'E']

def test_get_segment_directions_3():
    assert get_segment_directions(-1, -1, 4, (10, 10)) == []

def test_get_segment_directions_4():
    assert get_segment_directions(0, 10, 2, (10, 10)) == ['N']

def test_get_segment_directions_5():
    assert get_segment_directions(9, 0, 1, (10, 10)) == ['W']

def test_get_segment_directions_6():
    assert get_segment_directions(3, 7, 2, (10, 10)) == ['NW', 'NE']

def test_get_segment_directions_7():
    with pytest.raises(Exception):
        get_segment_directions(-1, -1, 4, (10, 10))
