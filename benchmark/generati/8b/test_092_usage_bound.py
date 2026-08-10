from funzione import usage_bound

def test_usage_bound_1():
    assert usage_bound([10, 20, 30], 3, 'raid0') == 10

def test_usage_bound_2():
    assert usage_bound([10, 20, 30], 3, 'raid1') == 10

def test_usage_bound_3():
    assert usage_bound([10, 20, 30], 3, 'raid5') == 10

def test_usage_bound_4():
    assert usage_bound([10, 20, 30], 3, 'raid6') == 10

def test_usage_bound_5():
    assert usage_bound([10, 20, 30], 3, 'raid10') == 10

def test_usage_bound_6():
    assert usage_bound([10, 20, 30], 3, 'single') == 10

def test_usage_bound_7():
    assert usage_bound([10, 20, 30], 3, 'raid0') == usage_bound([10, 20, 30], 3, 'raid0')

def test_usage_bound_8():
    assert usage_bound([10, 20, 30], 3, 'raid0') == usage_bound([10, 20, 30], 3, 'raid0')
