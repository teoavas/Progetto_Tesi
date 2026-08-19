import pytest
from funzione import BinaryFromFraction

def test_BinaryFromFraction_1():
    assert BinaryFromFraction(10, 2) == (0, 11, 52, True)

def test_BinaryFromFraction_2():
    assert BinaryFromFraction(-5, 3) == (-1, 12, 51, False)

def test_BinaryFromFraction_3():
    assert BinaryFromFraction(10000000000, 12345678901234567890) == (0, 11, 52, True)

def test_BinaryFromFraction_4():
    assert BinaryFromFraction(-1, 2) == (-1, 12, 51, False)

def test_BinaryFromFraction_5():
    assert BinaryFromFraction(10**10000000, 3**1000000) == (0, 11, 52, True)

def test_BinaryFromFraction_6():
    assert BinaryFromFraction(-1**10000000, 2**1000000) == (-1, 12, 51, False)

def test_BinaryFromFraction_7():
    assert BinaryFromFraction(10**-1023, 2**-1024) == (0, 11, 52, True)
