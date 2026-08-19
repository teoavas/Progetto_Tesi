from funzione import compute_convolution_output_dimensions
import math

def test_compute_convolution_output_dimensions_1():
    assert compute_convolution_output_dimensions(3, 2) == [2]

def test_compute_convolution_output_dimensions_2():
    assert compute_convolution_output_dimensions((3,), (2,)) == [2]

def test_compute_convolution_output_dimensions_3():
    assert compute_convolution_output_dimensions(3, 2, s=1) == [4]

def test_compute_convolution_output_dimensions_4():
    assert compute_convolution_output_dimensions((3,), (2,), s=(1,)) == [4]

def test_compute_convolution_output_dimensions_5():
    assert compute_convolution_output_dimensions(3, 2, p=0) == [2]

def test_compute_convolution_output_dimensions_6():
    assert compute_convolution_output_dimensions((3,), (2,), p=(0,)) == [2]

def test_compute_convolution_output_dimensions_7():
    assert compute_convolution_output_dimensions(3, 2, s=1, p=0) == [4]
