from funzione import windows_k_distinct

def test_windows_k_distinct_1():
    assert list(windows_k_distinct([1, 2, 3, 4, 5], 2)) == [(0, 1)]

def test_windows_k_distinct_2():
    assert list(windows_k_distinct([1, 1, 1, 1, 1], 2)) == []

def test_windows_k_distinct_3():
    assert list(windows_k_distinct([1, 2, 2, 3, 4], 2)) == [(0, 1)]

def test_windows_k_distinct_4():
    assert list(windows_k_distinct([1, 2, 3, 4, 5], 5)) == []

def test_windows_k_distinct_5():
    assert list(windows_k_distinct([1, 1, 1, 1, 1], 5)) == []

def test_windows_k_distinct_6():
    assert list(windows_k_distinct([], 2)) == []

def test_windows_k_distinct_7():
    assert list(windows_k_distinct([1, 2, 3, 4, 5], 0)) == []
