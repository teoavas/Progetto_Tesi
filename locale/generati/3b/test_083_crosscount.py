from funzione import crosscount

def test_crosscount_1():
    assert crosscount([1, 2, 3, 4]) == 0

def test_crosscount_2():
    assert round(crosscount([5, 6, 7, 8]), 2) == 0.00

def test_crosscount_3():
    assert crosscount([9, 10, 11, 12]) == 1

def test_crosscount_4():
    assert round(crosscount([13, 14, 15, 16]), 2) == 0.25

def test_crosscount_5():
    assert crosscount([17, 18, 19, 20]) == 2

def test_crosscount_6():
    assert round(crosscount([21, 22, 23, 24]), 2) == 0.50

def test_crosscount_7():
    assert crosscount([25, 26, 27, 28]) == 3
