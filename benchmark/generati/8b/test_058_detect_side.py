from funzione import detect_side

def test_detect_side_1():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 1, 'lng': 1}
    degrees = 0
    assert detect_side(start, point, degrees) == '0 degress'

def test_detect_side_2():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 1, 'lng': 1}
    degrees = 90
    assert detect_side(start, point, degrees) == '180 degrees right'

def test_detect_side_3():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 0, 'lng': 1}
    degrees = 0
    assert detect_side(start, point, degrees) == '0 degress right'

def test_detect_side_4():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 0, 'lng': -1}
    degrees = 0
    assert detect_side(start, point, degrees) == '0 degress left'

def test_detect_side_5():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 1, 'lng': 0}
    degrees = 0
    assert detect_side(start, point, degrees) == '0 degrees right'

def test_detect_side_6():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': -1, 'lng': 0}
    degrees = 0
    assert detect_side(start, point, degrees) == '0 degrees left'

def test_detect_side_7():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 0, 'lng': 0}
    degrees = 0
    assert detect_side(start, point, degrees) == '0 degress'
