import math
from funzione import common_conv2d_pool_output_shape

def test_common_conv2d_pool_output_shape_1():
    assert common_conv2d_pool_output_shape(3, 1, 1, 'SAME') == (3, 4, 4, 1)
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(3, 1, 1, 'INVALID')
    assert common_conv2d_pool_output_shape(5, 1, 1, 'SAME') == (5, 4, 4, 1)

def test_common_conv2d_pool_output_shape_2():
    assert common_conv2d_pool_output_shape(3, 1, 1, 'VALID') == (3, 4, 4, 1)
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(3, 1, 1, 'INVALID')
    assert common_conv2d_pool_output_shape(5, 1, 1, 'SAME') == (5, 4, 4, 1)

def test_common_conv2d_pool_output_shape_3():
    assert common_conv2d_pool_output_shape(3, 1, 1, 'SAME') == (3, 4, 4, 1)
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(3, 1, 1, 'INVALID')
    assert common_conv2d_pool_output_shape(5, 1, 1, 'VALID') == (5, 4, 4, 1)

def test_common_conv2d_pool_output_shape_4():
    assert common_conv2d_pool_output_shape(3, 1, 1, 'SAME') == (3, 4, 4, 1)
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(3, 1, 1, 'INVALID')
    assert common_conv2d_pool_output_shape(5, 1, 1, 'VALID') == (5, 4, 4, 1)

def test_common_conv2d_pool_output_shape_5():
    assert common_conv2d_pool_output_shape(3, 1, 1, 'SAME') == (3, 4, 4, 1)
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(3, 1, 1, 'INVALID')
    assert common_conv2d_pool_output_shape(5, 1, 1, 'VALID') == (5, 4, 4, 1)

def test_common_conv2d_pool_output_shape_6():
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(3, 1, 1, 'INVALID')
    assert common_conv2d_pool_output_shape(5, 1, 1, 'SAME') == (5, 4, 4, 1)

def test_common_conv2d_pool_output_shape_7():
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(3, 1, 1, 'INVALID')
    assert common_conv2d_pool_output_shape(5, 1, 1, 'SAME') == (5, 4, 4, 1)

def test_common_conv2d_pool_output_shape_8():
    with pytest.raises(ValueError):
        common_conv2d_pool_output_shape(3, 1, 1, 'INVALID')
    assert common_conv2d_pool_output_shape(5, 1, 1, 'SAME') == (5, 4, 4, 1)
