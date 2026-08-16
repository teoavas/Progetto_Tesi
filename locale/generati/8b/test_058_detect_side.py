from funzione import detect_side

def test_detect_side_1():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 10, 'lng': 20}
    degrees = 45
    assert detect_side(start, point, degrees) == f'{degrees} degrees right'

def test_detect_side_2():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': -10, 'lng': -20}
    degrees = 135
    assert detect_side(start, point, degrees) == f'{degrees + 90} degrees left'

def test_detect_side_3():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 10, 'lng': -20}
    degrees = 45
    assert detect_side(start, point, degrees) == f'{degrees} degrees right'

def test_detect_side_4():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': -10, 'lng': 20}
    degrees = 135
    assert detect_side(start, point, degrees) == f'{degrees + 90} degrees left'

def test_detect_side_5():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 0, 'lng': 10}
    degrees = 45
    assert detect_side(start, point, degrees) == f'{degrees} degress right'

def test_detect_side_6():
    start = {'lat': 0, 'lng': 0}
    point = {'lat': 0, 'lng': -10}
    degrees = 135
    assert detect_side(start, point, degrees) == f'{degrees} degress left'
