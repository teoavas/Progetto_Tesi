from funzione import can_blas

def test_can_blas_1():
    inputs = [[1, 2], [3, 4]]
    result = 'TDOT'
    idx_removed = set([0])
    assert can_blas(inputs, result, idx_removed) == True

def test_can_blas_2():
    inputs = [[1, 2], [3, 4]]
    result = 'GEMM'
    idx_removed = set([0])
    assert can_blas(inputs, result, idx_removed) == False

def test_can_blas_3():
    inputs = [[1, 2], [3, 4]]
    result = 'TDOT'
    idx_removed = set()
    assert can_blas(inputs, result, idx_removed) == False

def test_can_blas_4():
    inputs = [[1, 2, 3], [4, 5, 6]]
    result = 'GEMM'
    idx_removed = set([0])
    assert can_blas(inputs, result, idx_removed) == True

def test_can_blas_5():
    inputs = [[1, 2], [3, 4]]
    result = 'TDOT'
    idx_removed = set([1])
    assert can_blas(inputs, result, idx_removed) == False

def test_can_blas_6():
    inputs = [[1, 2], [3, 4]]
    result = 'GEMM'
    idx_removed = set()
    assert can_blas(inputs, result, idx_removed) == True
