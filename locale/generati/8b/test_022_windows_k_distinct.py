from funzione import windows_k_distinct

def test_windows_k_distinct_1():
    result = list(windows_k_distinct([1, 2, 3, 4], 2))
    assert len(result) == 2
    assert result[0] == (0, 2)
    assert result[1] == (1, 3)

def test_windows_k_distinct_2():
    result = list(windows_k_distinct([1, 1, 1, 1], 1))
    assert len(result) == 4
    assert result[0] == (0, 1)
    assert result[1] == (1, 2)
    assert result[2] == (2, 3)
    assert result[3] == (3, 4)

def test_windows_k_distinct_3():
    result = list(windows_k_distinct([1, 2, 2, 3, 3, 3], 2))
    assert len(result) == 3
    assert result[0] == (0, 2)
    assert result[1] == (1, 4)
    assert result[2] == (2, 6)

def test_windows_k_distinct_4():
    result = list(windows_k_distinct([1, 1, 1, 1], 3))
    assert len(result) == 0

def test_windows_k_distinct_5():
    result = list(windows_k_distinct([], 2))
    assert len(result) == 0
