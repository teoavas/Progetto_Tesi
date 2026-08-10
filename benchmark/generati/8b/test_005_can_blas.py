from funzione import can_blas

def test_can_blas_1():
    assert can_blas([1, 2, 3], [4, 5, 6], [0]) == False

def test_can_blas_2():
    assert can_blas([1, 2, 3], [4, 5, 6], [1]) == False

def test_can_blas_3():
    assert can_blas([1, 2, 3], [4, 5, 6], [2]) == False

def test_can_blas_4():
    assert can_blas([1, 2, 3], [4, 5, 6], [0, 1]) == False

def test_can_blas_5():
    assert can_blas([1, 2, 3], [4, 5, 6], [0, 2]) == False

def test_can_blas_6():
    assert can_blas([1, 2, 3], [4, 5, 6], [1, 2]) == False

def test_can_blas_7():
    assert can_blas([1, 2, 3], [1, 2, 3], []) == 'DOT'

def test_can_blas_8():
    assert can_blas([1, 2, 3], [1, 2, 3], [0]) == False

def test_can_blas_9():
    assert can_blas([1, 2, 3], [4, 5, 6], []) == False

def test_can_blas_10():
    assert can_blas([1, 2, 3], [4, 5, 6], [0, 1]) == 'GEMM'

def test_can_blas_11():
    assert can_blas([1, 2, 3], [4, 5, 6], [1, 2]) == False

def test_can_blas_12():
    assert can_blas([1, 2, 3], [4, 5, 6], [0, 2]) == 'GEMM'

def test_can_blas_13():
    assert can_blas([1, 2, 3], [4, 5, 6], [1, 3]) == False

def test_can_blas_14():
    assert can_blas([1, 2, 3], [4, 5, 6], [0, 3]) == False

def test_can_blas_15():
    assert can_blas([1, 2, 3], [4, 5, 6], [1, 3]) == False

def test_can_blas_16():
    assert can_blas([1, 2, 3], [4, 5, 6], [0, 3]) == False

def test_can_blas_17():
    assert can_blas([1, 2, 3], [4, 5, 6], []) == False

def test_can_blas_18():
    assert can_blas([1, 2, 3], [4, 5, 6], [0]) == False

def test_can_blas_19():
    assert can_blas([1, 2, 3], [4, 5, 6], [1]) == False

def test_can_blas_20():
    assert can_blas([1, 2, 3], [4, 5, 6], [2]) == False
