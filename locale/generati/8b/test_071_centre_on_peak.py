from funzione import centre_on_peak
import sys

def test_centre_on_peak_1():
    data = [1, 2, 3, 4, 5]
    expected_result = [2, 3, 4, 5, 1]
    assert centre_on_peak(data) == expected_result

def test_centre_on_peak_2():
    data = [10, 20, 30, 40, 50]
    expected_result = [25, 30, 40, 50, 10]
    assert centre_on_peak(data) == expected_result

def test_centre_on_peak_3():
    data = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected_result = [3.0, 4.0, 5.0, 5.5, 1.5]
    assert centre_on_peak(data) == expected_result

def test_centre_on_peak_4():
    data = []
    expected_result = []
    assert centre_on_peak(data) == expected_result

def test_centre_on_peak_5():
    data = None
    expected_result = []
    assert centre_on_peak(data) == expected_result

def test_centre_on_peak_6():
    data = [1, 2]
    expected_result = [1, 2]
    assert centre_on_peak(data) == expected_result

def test_centre_on_peak_7():
    data = [10, 20, 30, 40, 50, 60]
    expected_result = [25.0, 30.0, 40.0, 50.0, 60.0, 10]
    assert centre_on_peak(data) == expected_result
