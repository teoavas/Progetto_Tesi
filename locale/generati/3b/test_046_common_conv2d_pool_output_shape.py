from funzione import common_conv2d_pool_output_shape
import math

def test_common_conv2d_pool_output_shape_1():
    assert common_conv2d_pool_output_shape((1, 32, 32, 3), (1, 3, 3, 64), (1, 1, 1, 1), 'SAME') == (1, 16, 16, 64)

def test_common_conv2d_pool_output_shape_2():
    assert common_conv2d_pool_output_shape((1, 32, 32, 3), (1, 3, 3, 64), (1, 2, 2, 1), 'SAME') == (1, 16, 14, 64)

def test_common_conv2d_pool_output_shape_3():
    assert common_conv2d_pool_output_shape((1, 32, 32, 3), (1, 3, 3, 64), (1, 1, 1, 1), 'VALID') == (1, 31, 31, 64)

def test_common_conv2d_pool_output_shape_4():
    assert common_conv2d_pool_output_shape((1, 32, 32, 3), (1, 3, 3, 64), (1, 2, 2, 1), 'VALID') == (1, 30, 29, 64)

def test_common_conv2d_pool_output_shape_5():
    assert common_conv2d_pool_output_shape((1, 32, 32, 3), (1, 3, 3, 64), (2, 2, 2, 1), 'SAME') == (1, 15, 15, 64)

def test_common_conv2d_pool_output_shape_6():
    assert common_conv2d_pool_output_shape((1, 32, 32, 3), (1, 3, 3, 64), (2, 2, 2, 1), 'VALID') == (1, 30, 29, 64)

def test_common_conv2d_pool_output_shape_7():
    assert common_conv2d_pool_output_shape((1, 32, 32, 3), (1, 3, 3, 64), (1, 1, 1, 1), padding='VALID') == (1, 31, 31, 64)
