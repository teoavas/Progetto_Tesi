from funzione import find_repeat

def test_find_repeat_1():
    assert find_repeat(['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']) == ['up', 'down', 'left', 'right']

def test_find_repeat_2():
    assert find_repeat(['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']) == ['up', 'down', 'left', 'right']

def test_find_repeat_3():
    assert find_repeat(['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']) == ['up', 'down', 'left', 'right']

def test_find_repeat_4():
    assert find_repeat(['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']) == ['up', 'down', 'left', 'right']

def test_find_repeat_5():
    assert find_repeat(['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']) == ['up', 'down', 'left', 'right']

def test_find_repeat_6():
    assert find_repeat(['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']) == ['up', 'down', 'left', 'right']

def test_find_repeat_7():
    assert find_repeat(['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']) == ['up', 'down', 'left', 'right']

def test_find_repeat_8():
    assert find_repeat(['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']) == ['up', 'down', 'left', 'right']
