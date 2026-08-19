import sys
import pytest

def test_centre_on_peak_1():
    assert centre_on_peak([10, 20, 30]) == [10, 20, 30]
    assert centre_on_peak([5, 15, 25]) == [5, 15, 25]

def test_centre_on_peak_2():
    assert centre_on_peak([-1, -3, -5]) == [-1, -3, -5]
    assert centre_on_peak([0, 0, 0]) == [0, 0, 0]

def test_centre_on_peak_3():
    assert centre_on_peak([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]
    assert centre_on_peak([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_centre_on_peak_4():
    assert centre_on_peak([10.0, 20.0, 30.0]) == [10.0, 20.0, 30.0]
    assert centre_on_peak([-1.0, -2.0, -3.0]) == [-1.0, -2.0, -3.0]

def test_centre_on_peak_5():
    with pytest.raises(ValueError):
        centre_on_peak(None)

def test_centre_on_peak_6():
    assert centre_on_peak([]) == []

def test_centre_on_peak_7():
    assert centre_on_peak([1]) == [1]
