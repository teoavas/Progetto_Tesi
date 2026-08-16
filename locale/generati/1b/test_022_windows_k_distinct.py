import pytest

def test_windows_k_distinct_1():
    assert set(windows_k_distinct([1, 2, 3], 2)) == {(0, 1)}

def test_windows_k_distinct_2():
    assert set(windows_k_distinct([4, 5, 6, 7], 3)) == {(0, 1, 2)}

def test_windows_k_distinct_3():
    assert set(windows_k_distinct([8, 9, 10, 11], 4)) == {(0, 1, 2, 3)}

def test_windows_k_distinct_4():
    assert set(windows_k_distinct([12, 13, 14, 15], 5)) == {(0, 1, 2, 3, 4)}

def test_windows_k_distinct_5():
    assert set(windows_k_distinct([16, 17, 18, 19, 20], 6)) == {(0, 1, 2, 3, 4, 5)}

def test_windows_k_distinct_6():
    assert set(windows_k_distinct([21, 22, 23, 24, 25, 26], 7)) == {(0, 1, 2, 3, 4, 5, 6)}

def test_windows_k_distinct_7():
    assert set(windows_k_distinct([27, 28, 29, 30, 31, 32, 33], 8)) == {(0, 1, 2, 3, 4, 5, 6, 7)}

def test_windows_k_distinct_8():
    assert set(windows_k_distinct([34, 35, 36, 37, 38, 39, 40], 9)) == {(0, 1, 2, 3, 4, 5, 6, 7, 8)}
