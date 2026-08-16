from funzione import centre_on_peak
import sys

def test_centre_on_peak_1():
    assert len(centre_on_peak([1, 2, 3, 4, 5])) == 5

def test_centre_on_peak_2():
    assert centre_on_peak([]) == []

def test_centre_on_peak_3():
    assert centre_on_peak(None) == []

def test_centre_on_peak_4():
    data = [1, 2, 3, 4, 5]
    assert centre_on_peak(data) == [3, 4, 5, 4, 3]

def test_centre_on_peak_5():
    data = [1, 2, 3, 4, 5, 6]
    assert len(centre_on_peak(data)) == 6

def test_centre_on_peak_6():
    data = [1, 2, 3, 4, 5, 6, 7]
    assert centre_on_peak(data) == [4, 5, 6, 7, 6, 5, 4]

def test_centre_on_peak_7():
    data = [10, 20, 30, 40, 50, 60, 70, 80]
    assert centre_on_peak(data) == [40, 50, 60, 70, 80, 70, 60, 50]
