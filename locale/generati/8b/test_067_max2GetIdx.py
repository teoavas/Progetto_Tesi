from funzione import max2GetIdx

def test_max2GetIdx_1():
    A = [3, 5, 7]
    lo = 0
    hi = 3
    assert max2GetIdx(A, lo, hi) == (1, 2)

def test_max2GetIdx_2():
    A = [10, 20, 30, 40, 50]
    lo = 0
    hi = 5
    assert max2GetIdx(A, lo, hi) == (3, 4)

def test_max2GetIdx_3():
    A = [1, 2, 3, 4, 5]
    lo = 0
    hi = 5
    assert max2GetIdx(A, lo, hi) == (4, 4)

def test_max2GetIdx_4():
    A = [10, 20, 30, 40, 50, 60]
    lo = 0
    hi = 6
    assert max2GetIdx(A, lo, hi) == (5, 5)

def test_max2GetIdx_5():
    A = [1, 3, 5, 7, 9, 11, 13, 15]
    lo = 0
    hi = 8
    assert max2GetIdx(A, lo, hi) == (6, 7)

def test_max2GetIdx_6():
    A = [10, 20, 30, 40, 50, 60, 70, 80]
    lo = 0
    hi = 8
    assert max2GetIdx(A, lo, hi) == (6, 7)

def test_max2GetIdx_7():
    A = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    lo = 0
    hi = 9
    assert max2GetIdx(A, lo, hi) == (8, 8)

def test_max2GetIdx_8():
    A = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    lo = 0
    hi = 9
    assert max2GetIdx(A, lo, hi) == (8, 8)
