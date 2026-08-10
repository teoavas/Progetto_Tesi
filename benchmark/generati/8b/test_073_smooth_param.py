from funzione import smooth_param

def test_smooth_param_1():
    assert smooth_param([1, 2, 3], 'very_rough') == (1, 6, 0, 0, 'interp')

def test_smooth_param_2():
    assert smooth_param([1, 2, 3], 'rough') == (1, 5, 0, 0, 'interp')

def test_smooth_param_3():
    assert smooth_param([1, 2, 3], 'middle') == (1, 3, 0, 0, 'interp')

def test_smooth_param_4():
    assert smooth_param([1, 2, 3], 'fine') == (1, 2, 0, 0, 'interp')

def test_smooth_param_5():
    assert smooth_param([1, 2, 3], 'very_fine') == (1, 1, 0, 0, 'interp')

def test_smooth_param_6():
    assert smooth_param([1, 2, 3], 'invalid') == (1, 6, 0, 0, 'interp')

def test_smooth_param_7():
    assert smooth_param([], 'very_rough') == (150, 6, 0, 0, 'interp')

def test_smooth_param_8():
    assert smooth_param([1, 2, 3], 'very_rough') == (1, 6, 0, 0, 'interp')
