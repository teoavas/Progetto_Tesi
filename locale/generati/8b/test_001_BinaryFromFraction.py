from funzione import BinaryFromFraction

def test_BinaryFromFraction_1():
    result = BinaryFromFraction(10, 2)
    assert result[0] == 5
    assert result[1] == 3
    assert result[2] == 52
    assert result[3]

def test_BinaryFromFraction_2():
    result = BinaryFromFraction(-10, 2)
    assert result[0] == 2147483647
    assert result[1] == -1021
    assert result[2] == 52
    assert not result[3]

def test_BinaryFromFraction_3():
    result = BinaryFromFraction(0, 10)
    assert result[0] == 0
    assert result[1] == -1022
    assert result[2] == 52
    assert True

def test_BinaryFromFraction_4():
    result = BinaryFromFraction(10, 0)
    assert result[0] is None
    assert result[1] is None
    assert result[2] is None
    assert False

def test_BinaryFromFraction_5():
    result = BinaryFromFraction(-10, -2)
    assert result[0] == 2147483647
    assert result[1] == -1021
    assert result[2] == 52
    assert not result[3]

def test_BinaryFromFraction_6():
    result = BinaryFromFraction(10, 4)
    assert result[0] == 5
    assert result[1] == 3
    assert result[2] == 52
    assert True

def test_BinaryFromFraction_7():
    result = BinaryFromFraction(-10, -4)
    assert result[0] == 2147483647
    assert result[1] == -1021
    assert result[2] == 52
    assert not result[3]
