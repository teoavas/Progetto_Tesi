from funzione import can_blas

def test_can_blas_1():
    assert can_blas([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], []) == 'GEMM'

def test_can_blas_2():
    assert can_blas([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], [{'a': 1, 'b': 2}, {'e': 5, 'f': 6}], []) == False

def test_can_blas_3():
    assert can_blas([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], [1]) == False

def test_can_blas_4():
    assert can_blas([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], [1, 2]) == False

def test_can_blas_5():
    assert can_blas([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], []) == False

def test_can_blas_6():
    assert can_blas([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], [{'a': 1, 'b': 2}, {'e': 5, 'f': 6}], [1]) == False

def test_can_blas_7():
    assert can_blas([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}], [{'a': 1, 'b': 2}, {'e': 5, 'f': 6}], [1, 2]) == False
