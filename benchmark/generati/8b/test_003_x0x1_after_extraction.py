from funzione import x0x1_after_extraction

def test_x0x1_after_extraction_1():
    assert x0x1_after_extraction(10, 20, 15, 25) == (0, 10)

def test_x0x1_after_extraction_2():
    assert x0x1_after_extraction(10, 20, 5, 25) == (5, 20)

def test_x0x1_after_extraction_3():
    assert x0x1_after_extraction(10, 20, 25, 25) == (0, 0)

def test_x0x1_after_extraction_4():
    assert x0x1_after_extraction(10, 20, 30, 25) == (0, 15)

def test_x0x1_after_extraction_5():
    assert x0x1_after_extraction(10, 20, 35, 25) == (0, 0)

def test_x0x1_after_extraction_6():
    assert x0x1_after_extraction(10, 20, 10, 25) == (0, 15)

def test_x0x1_after_extraction_7():
    assert x0x1_after_extraction(10, 20, 0, 25) == (10, 25)

def test_x0x1_after_extraction_8():
    assert x0x1_after_extraction(10, 20, 10, 10) == (None, None)
