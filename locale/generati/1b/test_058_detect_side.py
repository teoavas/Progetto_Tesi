import pytest

def test_detect_side_1():
    assert detect_side({'lat': 37.7749, 'lng': -122.4194}, {'lat': 37.7858, 'lng': -122.4364}, 90) == "180 degrees right"

def test_detect_side_2():
    assert detect_side({'lat': 40.7128, 'lng': -74.0060}, {'lat': 40.7238, 'lng': -73.9857}, 45) == "135 degrees left"

def test_detect_side_3():
    assert detect_side({'lat': 51.5074, 'lng': -0.1278}, {'lat': 51.5086, 'lng': -0.1282}, 90) == "270 degrees right"

def test_detect_side_4():
    assert detect_side({'lat': 37.7749, 'lng': -122.4194}, {'lat': 37.7858, 'lng': -122.4364}, 180) == "0 degrees right"

def test_detect_side_5():
    assert detect_side({'lat': 40.7128, 'lng': -74.0060}, {'lat': 40.7238, 'lng': -73.9857}, 45) == "135 degrees left"

def test_detect_side_6():
    assert detect_side({'lat': 51.5074, 'lng': -0.1278}, {'lat': 51.5086, 'lng': -0.1282}, 90) == "270 degrees right"

def test_detect_side_7():
    assert detect_side({'lat': 37.7749, 'lng': -122.4194}, {'lat': 37.7858, 'lng': -122.4364}, 360) == "0 degrees right"

def test_detect_side_8():
    assert detect_side({'lat': 40.7128, 'lng': -74.0060}, {'lat': 40.7238, 'lng': -73.9857}, 90) == "180 degrees right"
