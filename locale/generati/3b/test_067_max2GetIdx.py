from funzione import max2GetIdx

def test_max2GetIdx_1():
    A = [1, 2, 3, 4, 5]
    lo, hi = 0, len(A) - 1
    assert max2GetIdx(A, lo, hi) == (0, 4)

def test_max2GetIdx_2():
    A = [5, 4, 3, 2, 1]
    lo, hi = 0, len(A) - 1
    assert max2GetIdx(A, lo, hi) == (0, 0)

def test_max2GetIdx_3():
    A = [1, 2, 3, 4, 5]
    lo, hi = 0, 4
    assert max2GetIdx(A, lo, hi) == (0, 4)

def test_max2GetIdx_4():
    A = [1, 2, 3, 4, 5]
    lo, hi = 1, 4
    assert max2GetIdx(A, lo, hi) == (1, 4)

def test_max2GetIdx_5():
    A = [1, 2, 3, 4, 5]
    lo, hi = 0, 2
    assert max2GetIdx(A, lo, hi) == (0, 2)

def test_max2GetIdx_6():
    A = [1, 2, 3, 4, 5]
    lo, hi = 2, 4
    assert max2GetIdx(A, lo, hi) == (2, 4)

def test_max2GetIdx_7():
    A = [1, 2, 3, 4, 5]
    lo, hi = 0, 1
    with pytest.raises(IndexError):
        max2GetIdx(A, lo, hi)
