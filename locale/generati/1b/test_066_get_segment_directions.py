import pytest

def test_get_segment_directions_1():
    assert get_segment_directions(0, 0, 2, (10, 20)) == ['N', 'E']

def test_get_segment_directions_2():
    with pytest.raises(Exception):
        get_segment_directions(-5, -3, 4, (10, 20))

def test_get_segment_directions_3():
    assert get_segment_directions(0, 1, 2, (10, 20)) == ['NE', 'E']

def test_get_segment_directions_4():
    with pytest.raises(Exception):
        get_segment_directions(-5, -6, 4, (10, 20))

def test_get_segment_directions_5():
    assert get_segment_directions(0, 0, 1, (10, 20)) == ['N', 'NE']

def test_get_segment_directions_6():
    with pytest.raises(Exception):
        get_segment_directions(-5, -4, 4, (10, 20))

def test_get_segment_directions_7():
    assert get_segment_directions(0, 1, 3, (10, 20)) == ['NE', 'SE']

def test_get_segment_directions_8():
    with pytest.raises(Exception):
        get_segment_directions(-5, -2, 4, (10, 20))
