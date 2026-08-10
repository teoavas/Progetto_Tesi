from funzione import common_conv2d_pool_output_shape
import math

def test_common_conv2d_pool_output_shape_1():
    input_NHWC = (1, 10, 10, 1)
    filter_HWIO = (1, 3, 3, 1)
    stride_NHWC = (1, 2, 2, 1)
    padding = 'SAME'
    assert common_conv2d_pool_output_shape(input_NHWC, filter_HWIO, stride_NHWC, padding) == (1, 5, 5, 1)

def test_common_conv2d_pool_output_shape_2():
    input_NHWC = (1, 10, 10, 1)
    filter_HWIO = (1, 3, 3, 1)
    stride_NHWC = (1, 1, 1, 1)
    padding = 'SAME'
    assert common_conv2d_pool_output_shape(input_NHWC, filter_HWIO, stride_NHWC, padding) == (1, 10, 10, 1)

def test_common_conv2d_pool_output_shape_3():
    input_NHWC = (1, 10, 10, 1)
    filter_HWIO = (1, 3, 3, 1)
    stride_NHWC = (1, 2, 2, 1)
    padding = 'VALID'
    assert common_conv2d_pool_output_shape(input_NHWC, filter_HWIO, stride_NHWC, padding) == (1, 5, 5, 1)

def test_common_conv2d_pool_output_shape_4():
    input_NHWC = (1, 10, 10, 1)
    filter_HWIO = (1, 3, 3, 1)
    stride_NHWC = (1, 1, 1, 1)
    padding = 'VALID'
    assert common_conv2d_pool_output_shape(input_NHWC, filter_HWIO, stride_NHWC, padding) == (1, 8, 8, 1)

def test_common_conv2d_pool_output_shape_5():
    input_NHWC = (1, 10, 10, 1)
    filter_HWIO = (1, 3, 3, 1)
    stride_NHWC = (1, 2, 2, 1)
    padding = 'SAME'
    assert common_conv2d_pool_output_shape(input_NHWC, filter_HWIO, stride_NHWC, padding) != (1, 6, 6, 1)

def test_common_conv2d_pool_output_shape_6():
    input_NHWC = (1, 10, 10, 1)
    filter_HWIO = (1, 3, 3, 1)
    stride_NHWC = (1, 2, 2, 1)
    padding = 'VALID'
    assert common_conv2d_pool_output_shape(input_NHWC, filter_HWIO, stride_NHWC, padding) != (1, 7, 7, 1)

def test_common_conv2d_pool_output_shape_7():
    input_NHWC = (1, 10, 10, 1)
    filter_HWIO = (1, 3, 3, 1)
    stride_NHWC = (1, 2, 2, 1)
    padding = 'SAME'
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(input_NHWC, filter_HWIO, stride_NHWC, 'INVALID')

def test_common_conv2d_pool_output_shape_8():
    input_NHWC = (1, 10, 10, 1)
    filter_HWIO = (1, 3, 3, 1)
    stride_NHWC = (1, 2, 2, 1)
    padding = 'SAME'
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(input_NHWC, filter_HWIO, (1, 2, 2, 3), padding)
