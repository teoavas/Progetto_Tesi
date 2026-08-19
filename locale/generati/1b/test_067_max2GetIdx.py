import pytest

def test_max2GetIdx_1():
    A = [5, 3, 8, 4, 2]
    lo, hi = 0, len(A) - 1
    x1, x2 = max2GetIdx(A, lo, hi)
    assert x1 == 2 and x2 == 3

def test_max2GetIdx_2():
    A = [5, 3, 8, 4, 2]
    lo, hi = 0, len(A) - 1
    with pytest.raises(IndexError):
        max2GetIdx(A, lo, hi)

def test_max2GetIdx_3():
    A = [5, 3, 8, 4, 2]
    lo, hi = 0, len(A) - 1
    x1, x2 = max2GetIdx(A, lo, hi)
    assert x1 == 0 and x2 == 1

def test_max2GetIdx_4():
    A = [5, 3, 8, 4, 2]
    lo, hi = 0, len(A) - 1
    with pytest.raises(IndexError):
        max2GetIdx(A, lo, hi)

def test_max2GetIdx_5():
    A = [5, 3, 8, 4, 2]
    lo, hi = 0, len(A) - 1
    x1, x2 = max2GetIdx(A, lo, hi)
    assert x1 == 0 and x2 == 1

def test_max2GetIdx_6():
    A = [5, 3, 8, 4, 2]
    lo, hi = 0, len(A) - 1
    with pytest.raises(IndexError):
        max2GetIdx(A, lo, hi)

def test_max2GetIdx_7():
    A = [5, 3, 8, 4, 2]
    lo, hi = 0, len(A) - 1
    x1, x2 = max2GetIdx(A, lo, hi)
    assert x1 == 0 and x2 == 1

def test_max2GetIdx_8():
    A = [5, 3, 8, 4, 2]
    lo, hi = 0, len(A) - 1
    with pytest.raises(IndexError):
        max2GetIdx(A, lo, hi)
