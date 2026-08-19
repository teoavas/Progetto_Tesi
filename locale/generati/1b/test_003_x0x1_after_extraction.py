import pytest

def test_x0x1_after_extraction_1():
    assert x0x1_after_extraction(10, 5, 15, 20) == (10, 15)

def test_x0x1_after_extraction_2():
    assert x0x1_after_extraction(25, 5, 30, 35) is None

def test_x0x1_after_extraction_3():
    assert x0x1_after_extraction(-10, -5, -15, -20) == (None, None)

def test_x0x1_after_extraction_4():
    assert x0x1_after_extraction(30, 25, 35, 40) is None

def test_x0x1_after_extraction_5():
    assert x0x1_after_extraction(-10, -15, -20, -25) == (None, None)

def test_x0x1_after_extraction_6():
    with pytest.raises(UnboundLocalError):
        x0x1_after_extraction(30, 35, 40, 45)

def test_x0x1_after_extraction_7():
    assert x0x1_after_extraction(-10, -15, -20, -25) == (None, None)
