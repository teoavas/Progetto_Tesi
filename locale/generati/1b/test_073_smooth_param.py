import pytest
from funzione import smooth_param

def test_smooth_param_1():
    assert smooth_param([10, 20, 30], 'very_rough') == [50, 6, 0, 0, 'interp']

def test_smooth_param_2():
    assert smooth_param([5, 15, 25], 'smooth') == [10, 3, 1, 0, 'interp']

def test_smooth_param_3():
    assert smooth_param([8, 16, 24], 'very_fine') == [12, 1, 0, 0, 'interp')

def test_smooth_param_4():
    assert smooth_param([2, 6, 10], 'fine') == [5, 2, 0, 0, 'interp')

def test_smooth_param_5():
    assert smooth_param([3, 9, 15], 'very_rough') == [20, 6, 1, 0, 'interp']

def test_smooth_param_6():
    assert smooth_param([7, 19, 29], 'smooth') == [14, 4, 2, 0, 'interp')

def test_smooth_param_7():
    assert smooth_param([11, 23, 35], 'very_fine') == [18, 1, 0, 0, 'interp')

def test_smooth_param_8():
    assert smooth_param([4, 12, 20], 'middle') == [10, 3, 2, 0, 'interp')
