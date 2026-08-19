from funzione import compute_convolution_output_dimensions
import math

def test_compute_convolution_output_dimensions_1():
    assert compute_convolution_output_dimensions(3, 5) == [2]

def test_compute_convolution_output_dimensions_2():
    assert compute_convolution_output_dimensions(4, 7, s=2) == [3]

def test_compute_convolution_output_dimensions_3():
    assert compute_convolution_output_dimensions(6, 9, p=1) == [5]

def test_compute_convolution_output_dimensions_4():
    assert compute_convolution_output_dimensions(8, 11, transposed=True) == [7]

def test_compute_convolution_output_dimensions_5():
    assert compute_convolution_output_dimensions((2,), (3,), s=[2], p=[1]) == [3]

def test_compute_convolution_output_dimensions_6():
    assert compute_convolution_output_dimensions(10, 13, s=3) == [4]

def test_compute_convolution_output_dimensions_7():
    assert compute_convolution_output_dimensions((5,), (7,), transposed=True) == [8]
