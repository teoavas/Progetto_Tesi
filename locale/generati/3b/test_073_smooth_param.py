from funzione import smooth_param

def test_smooth_param_1():
    assert smooth_param([1, 2, 3], 'very_rough') == [181, 6, 0, 0, 'interp']

def test_smooth_param_2():
    assert smooth_param([1, 2, 3], 'rough') == [90, 5, 0, 0, 'interp']

def test_smooth_param_3():
    assert smooth_param([1, 2, 3], 'middle') == [40, 3, 0, 0, 'interp']

def test_smooth_param_4():
    assert smooth_param([1, 2, 3], 'fine') == [15, 2, 0, 0, 'interp']

def test_smooth_param_5():
    assert smooth_param([1, 2, 3], 'very_fine') == [6, 1, 0, 0, 'interp']

def test_smooth_param_6():
    with pytest.raises(KeyError):
        smooth_param([1, 2, 3], 'invalid')

def test_smooth_param_7():
    assert smooth_param([], 'very_rough') == [150, 6, 0, 0, 'interp']
