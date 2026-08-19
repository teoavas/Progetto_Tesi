from funzione import x0x1_after_extraction

def test_x0x1_after_extraction_1():
    assert x0x1_after_extraction(10, 20, 5, 15) == (5, 5)

def test_x0x1_after_extraction_2():
    assert x0x1_after_extraction(-3, -4, 2, 6) == None, None

def test_x0x1_after_extraction_3():
    assert x0x1_after_extraction(10, 20, 25, 30) == None, None

def test_x0x1_after_extraction_4():
    assert x0x1_after_extraction(5, 5, 2, 6) == None, None

def test_x0x1_after_extraction_5():
    assert x0x1_after_extraction(10, 20, 30, 40) == (10, 10)

def test_x0x1_after_extraction_6():
    with pytest.raises(UnboundLocalError):
        x0x1_after_extraction(-3, -4, 2, 5)

def test_x0x1_after_extraction_7():
    assert x0x1_after_extraction(10, 20, 15, 25) == (5, 5)
