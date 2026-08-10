import pytest
from funzione import centre_on_peak
import numpy as np

def test_centre_on_peak_1():
    data = [1, 2, 3, 4, 5]
    expected = [2, 3, 4, 5, 1]
    assert centre_on_peak(data) == expected

def test_centre_on_peak_2():
    data = [5, 4, 3, 2, 1]
    expected = [2, 3, 4, 5, 1]
    assert centre_on_peak(data) == expected

def test_centre_on_peak_3():
    data = [1, 1, 1, 1, 1]
    expected = [1, 1, 1, 1, 1]
    assert centre_on_peak(data) == expected

def test_centre_on_peak_4():
    data = [1, 2, 3, 4, 5, 6]
    expected = [3, 4, 5, 6, 1, 2]
    assert centre_on_peak(data) == expected

def test_centre_on_peak_5():
    data = [1, 2, 3, 4, 5, 6, 7]
    expected = [3, 4, 5, 6, 1, 2, 7]
    assert centre_on_peak(data) == expected

def test_centre_on_peak_6():
    data = None
    expected = []
    assert centre_on_peak(data) == expected

def test_centre_on_peak_7():
    data = []
    expected = []
    assert centre_on_peak(data) == expected

def test_centre_on_peak_8():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [5, 6, 7, 8, 1, 2, 3, 4, 9]
    assert centre_on_peak(data) == expected
