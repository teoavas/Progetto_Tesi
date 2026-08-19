from funzione import BinaryFromFraction

def test_BinaryFromFraction_1():
    assert BinaryFromFraction(0, 1) == (0, 0, 52, False)

def test_BinaryFromFraction_2():
    with pytest.raises(AssertionError):
        BinaryFromFraction(0, 0)

def test_BinaryFromFraction_3():
    result = BinaryFromFraction(1, 1)
    assert result == (1, 0, 52, False)

def test_BinaryFromFraction_4():
    result = BinaryFromFraction(2, 1)
    assert result == (2, 0, 52, True)

def test_BinaryFromFraction_5():
    result = BinaryFromFraction(3, 1)
    assert result == (3, 0, 52, False)

def test_BinaryFromFraction_6():
    result = BinaryFromFraction(10, 2)
    assert result == (5.0, 1, 52, True)

def test_BinaryFromFraction_7():
    result = BinaryFromFraction(-1, 1)
    assert result == (-1, 0, 52, False)
