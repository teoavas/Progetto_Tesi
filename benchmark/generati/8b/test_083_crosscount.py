from funzione import crosscount
import math

def test_crosscount_1():
    v = [0, 0, 0, 0, 0, 0, 0, 0]
    assert crosscount(v) == 0

def test_crosscount_2():
    v = [0, 0, 10, 10, 0, 0, 10, 10]
    assert crosscount(v) == 0

def test_crosscount_3():
    v = [0, 0, 10, 10, 0, 0, 20, 20]
    assert crosscount(v) == 1

def test_crosscount_4():
    v = [0, 0, 10, 10, 0, 0, 10, 20]
    assert crosscount(v) == 0

def test_crosscount_5():
    v = [0, 0, 10, 10, 0, 0, 10, 10]
    assert crosscount(v) == 1

def test_crosscount_6():
    v = [0, 0, 10, 10, 0, 0, 10, 10, 0, 0, 10, 10]
    assert crosscount(v) == 3

def test_crosscount_7():
    v = [0, 0, 10, 10, 0, 0, 10, 10, 0, 0, 10, 10, 0, 0, 10, 10]
    assert crosscount(v) == 6
