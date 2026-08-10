from funzione import compute_convolution_output_dimensions
import math

def test_compute_convolution_output_dimensions_1():
    assert compute_convolution_output_dimensions(5, 3) == [2]

def test_compute_convolution_output_dimensions_2():
    assert compute_convolution_output_dimensions(5, 3, s=2) == [3]

def test_compute_convolution_output_dimensions_3():
    assert compute_convolution_output_dimensions(5, 3, p=1) == [3]

def test_compute_convolution_output_dimensions_4():
    assert compute_convolution_output_dimensions(5, 3, s=2, p=1) == [3]

def test_compute_convolution_output_dimensions_5():
    assert compute_convolution_output_dimensions(5, 3, s=2, p=1, transposed=True) == [9]

def test_compute_convolution_output_dimensions_6():
    assert compute_convolution_output_dimensions((5, 5), 3) == [2, 2]

def test_compute_convolution_output_dimensions_7():
    assert compute_convolution_output_dimensions((5, 5), 3, s=(2, 2)) == [3, 3]

def test_compute_convolution_output_dimensions_8():
    assert compute_convolution_output_dimensions((5, 5), 3, p=(1, 1)) == [3, 3]

def test_compute_convolution_output_dimensions_9():
    assert compute_convolution_output_dimensions((5, 5), 3, s=(2, 2), p=(1, 1)) == [3, 3]

def test_compute_convolution_output_dimensions_10():
    assert compute_convolution_output_dimensions((5, 5), 3, s=(2, 2), p=(1, 1), transposed=True) == [9, 9]
