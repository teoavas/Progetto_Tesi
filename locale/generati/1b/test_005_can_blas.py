import pytest

def test_can_blas_1():
    assert can_blas([1, 2], [3, 4], []) == False

def test_can_blas_2():
    assert can_blas([1, 2], [3, 4], [0]) == 'GEMM'

def test_can_blas_3():
    assert can_blas([1, 2], [3, 4], [1, 0]) == False

def test_can_blas_4():
    assert can_blas([1, 2], [3, 4], [1, 1]) == 'TDOT'

def test_can_blas_5():
    assert can_blas([1, 2], [3, 4], [0, 0]) == False

def test_can_blas_6():
    assert can_blas([1, 2], [3, 4], []) == 'DOT'

def test_can_blas_7():
    assert can_blas([1, 2], [3, 4], [1, 1, 0]) == False

def test_can_blas_8():
    assert can_blas([1, 2], [3, 4], [1, 1, 1]) == 'GEMM'
