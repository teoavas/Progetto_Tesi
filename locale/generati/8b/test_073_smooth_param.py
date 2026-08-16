from funzione import smooth_param

def test_smooth_param_1():
    x = [1, 2, 3]
    sm_degree = 'very_rough'
    assert smooth_param(x, sm_degree) == [8, 6, 0, 0, 'interp']

def test_smooth_param_2():
    x = [1, 2, 3]
    sm_degree = 'rough'
    assert smooth_param(x, sm_degree) == [4, 5, 0, 0, 'interp']

def test_smooth_param_3():
    x = [1, 2, 3]
    sm_degree = 'middle'
    assert smooth_param(x, sm_degree) == [7, 3, 0, 0, 'interp']

def test_smooth_param_4():
    x = [1, 2, 3]
    sm_degree = 'fine'
    assert smooth_param(x, sm_degree) == [5, 2, 0, 0, 'interp']

def test_smooth_param_5():
    x = [1, 2, 3]
    sm_degree = 'very_fine'
    assert smooth_param(x, sm_degree) == [2, 1, 0, 0, 'interp']

def test_smooth_param_6():
    x = []
    sm_degree = 'very_rough'
    assert smooth_param(x, sm_degree) == [8, 6, 0, 0, 'interp']

def test_smooth_param_7():
    x = [1, 2, 3]
    sm_degree = 'invalid'
    with pytest.raises(ValueError):
        smooth_param(x, sm_degree)
