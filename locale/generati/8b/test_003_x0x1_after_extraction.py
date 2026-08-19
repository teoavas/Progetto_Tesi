from funzione import x0x1_after_extraction

def test_x0x1_after_extraction_1():
    assert x0x1_after_extraction(10, 20, 5, 15) == (5, 10)

def test_x0x1_after_extraction_2():
    assert x0x1_after_extraction(10, 20, 25, 30) is None

def test_x0x1_after_extraction_3():
    assert x0x1_after_extraction(-10, -20, 5, 15) == (None, None)

def test_x0x1_after_extraction_4():
    assert x0x1_after_extraction(10, 20, 30, 40) == (0, 10)

def test_x0x1_after_extraction_5():
    assert x0x1_after_extraction(10, 20, -5, 15) == (None, None)

def test_x0x1_after_extraction_6():
    assert x0x1_after_extraction(-10, -20, 5, 30) == (None, None)
