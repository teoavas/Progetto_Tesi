from funzione import max2GetIdx

def test_max2GetIdx_1():
    A = [1, 2, 3, 4, 5]
    lo = 0
    hi = 5
    assert max2GetIdx(A, lo, hi) == (4, 5)

def test_max2GetIdx_2():
    A = [5, 4, 3, 2, 1]
    lo = 0
    hi = 5
    assert max2GetIdx(A, lo, hi) == (0, 1)

def test_max2GetIdx_3():
    A = [1, 1, 1, 1, 1]
    lo = 0
    hi = 5
    assert max2GetIdx(A, lo, hi) == (0, 1)

def test_max2GetIdx_4():
    A = [1, 2, 3, 4, 5]
    lo = 0
    hi = 3
    assert max2GetIdx(A, lo, hi) == (3, 4)

def test_max2GetIdx_5():
    A = [1, 2, 3, 4, 5]
    lo = 2
    hi = 5
    assert max2GetIdx(A, lo, hi) == (4, 5)

def test_max2GetIdx_6():
    A = [1, 2, 3, 4, 5]
    lo = 0
    hi = 2
    assert max2GetIdx(A, lo, hi) == (2, 3)

def test_max2GetIdx_7():
    A = [1, 2, 3, 4, 5]
    lo = 1
    hi = 4
    assert max2GetIdx(A, lo, hi) == (4, 5)

def test_max2GetIdx_8():
    A = [1, 2, 3, 4, 5]
    lo = 0
    hi = 1
    assert max2GetIdx(A, lo, hi) == (0, 1)

def test_max2GetIdx_9():
    A = [1, 2, 3, 4, 5]
    lo = 0
    hi = 0
    assert max2GetIdx(A, lo, hi) == (0, 0)

def test_max2GetIdx_10():
    A = [1, 2, 3, 4, 5]
    lo = 1
    hi = 1
    assert max2GetIdx(A, lo, hi) == (0, 0)

def test_max2GetIdx_11():
    A = [1, 2, 3, 4, 5]
    lo = 5
    hi = 5
    assert max2GetIdx(A, lo, hi) == (0, 0)

def test_max2GetIdx_12():
    A = [1, 2, 3, 4, 5]
    lo = 0
    hi = 6
    try:
        max2GetIdx(A, lo, hi)
        assert False
    except IndexError:
        assert True

def test_max2GetIdx_13():
    A = [1, 2, 3, 4, 5]
    lo = 6
    hi = 7
    try:
        max2GetIdx(A, lo, hi)
        assert False
    except IndexError:
        assert True
