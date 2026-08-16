from funzione import find_repeat

def test_find_repeat_1():
    directions = ['up', 'down', 'left', 'right']
    assert find_repeat(directions) == ['up']

def test_find_repeat_2():
    directions = ['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']
    assert find_repeat(directions) == ['up', 'down']

def test_find_repeat_3():
    directions = ['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down']
    assert find_repeat(directions) == ['up', 'down']

def test_find_repeat_4():
    directions = ['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']
    assert find_repeat(directions) == ['up', 'down']

def test_find_repeat_5():
    directions = ['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down']
    assert find_repeat(directions) == ['up', 'down']

def test_find_repeat_6():
    directions = ['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left']
    assert find_repeat(directions) == ['up']

def test_find_repeat_7():
    directions = ['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right']
    assert find_repeat(directions) == ['up', 'down']

def test_find_repeat_8():
    directions = ['up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up']
    assert find_repeat(directions) == ['up', 'down']
