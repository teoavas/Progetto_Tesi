from funzione import find_repeat

def test_find_repeat_1():
    assert find_repeat(['up', 'up', 'up', 'up']) == ['up']

def test_find_repeat_2():
    assert find_repeat(['down', 'down', 'down', 'down']) == ['down']

def test_find_repeat_3():
    assert find_repeat(['left', 'left', 'left', 'left']) == ['left']

def test_find_repeat_4():
    assert find_repeat(['right', 'right', 'right', 'right']) == ['right']

def test_find_repeat_5():
    assert find_repeat(['up', 'down', 'left', 'right']) == []

def test_find_repeat_6():
    assert find_repeat(['up', 'up', 'up', 'up', 'up']) == ['up']

def test_find_repeat_7():
    assert find_repeat(['a', 'b', 'c', 'd']) == []
