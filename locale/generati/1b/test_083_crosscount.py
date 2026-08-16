import pytest
from funzione import crosscount

def test_crosscount_1():
    assert crosscount('A', 'B') == 0

def test_crosscount_2():
    assert crosscount('C', 'D') == 0

def test_crosscount_3():
    assert crosscount('A', 'C') == 0

def test_crosscount_4():
    assert crosscount('B', 'D') == 0

def test_crosscount_5():
    assert crosscount('A', 'B') == 1

def test_crosscount_6():
    assert crosscount('C', 'D') == 2

def test_crosscount_7():
    assert crosscount('A', 'C') == 3

def test_crosscount_8():
    assert crosscount('B', 'D') == 4
