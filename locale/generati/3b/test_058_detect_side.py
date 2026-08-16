from funzione import detect_side

def test_detect_side_1():
    assert detect_side({'lat': 0, 'lng': 0}, {'lat': 10, 'lng': 20}, 90) == '90 degrees right'

def test_detect_side_2():
    assert detect_side({'lat': 0, 'lng': 0}, {'lat': 10, 'lng': -20}, 90) == '90 degrees left'

def test_detect_side_3():
    assert detect_side({'lat': 10, 'lng': 0}, {'lat': 0, 'lng': 20}, 90) == '180 degrees right'

def test_detect_side_4():
    assert detect_side({'lat': -10, 'lng': 0}, {'lat': 0, 'lng': 20}, 90) == '90 degrees left'

def test_detect_side_5():
    assert detect_side({'lat': 0, 'lng': 0}, {'lat': 0, 'lng': 0}, 0) == '0 degress'

def test_detect_side_6():
    assert detect_side({'lat': 10, 'lng': 20}, {'lat': 10, 'lng': -20}, 90) == '180 degrees right'

def test_detect_side_7():
    assert detect_side({'lat': 0, 'lng': 0}, {'lat': 10, 'lng': 20}, 180) == '180 degrees right'
