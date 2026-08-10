from funzione import BinaryFromFraction

def test_BinaryFromFraction_1():
    assert BinaryFromFraction(1, 2) == (1, 0, 52, False)

def test_BinaryFromFraction_2():
    assert BinaryFromFraction(1, 1) == (1, 0, 52, True)

def test_BinaryFromFraction_3():
    assert BinaryFromFraction(2, 1) == (1, 1, 52, False)

def test_BinaryFromFraction_4():
    assert BinaryFromFraction(0, 1) == (0, 0, 52, True)

def test_BinaryFromFraction_5():
    assert BinaryFromFraction(1, 0) == (0, 0, 52, False)

def test_BinaryFromFraction_6():
    assert BinaryFromFraction(1, 3) == (0, 0, 52, False)

def test_BinaryFromFraction_7():
    assert BinaryFromFraction(2**51, 1) == (1, 1021, 52, False)

def test_BinaryFromFraction_8():
    assert BinaryFromFraction(1, 2**52) == (0, 0, 52, False)
