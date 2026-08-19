import pytest

def test_get_text_point_at_line_1():
    assert get_text_point_at_line(0.5, (10, 20), (30, 40), 'left', 5) == (15.0, 25.0)

def test_get_text_point_at_line_2():
    assert get_text_point_at_line(0.3, (50, 60), (70, 80), 'right', 10) == (55.0, 75.0)

def test_get_text_point_at_line_3():
    assert get_text_point_at_line(0.1, (90, 100), (110, 120), 'top', 20) == (95.0, 115.0)

def test_get_text_point_at_line_4():
    assert get_text_point_at_line(0.2, (130, 150), (160, 170), 'bottom', 30) == (145.0, 175.0)

def test_get_text_point_at_line_5():
    assert get_text_point_at_line(0.6, (200, 220), (210, 230), 'center', 40) == (205.0, 225.0)

def test_get_text_point_at_line_6():
    assert get_text_point_at_line(0.4, (250, 270), (260, 280), 'left', 50) == (255.0, 275.0)
