from funzione import rollDie
import random

def test_rollDie_1():
    result = rollDie('red')
    assert isinstance(result, dict)
    assert 'color' in result and 'icon' in result

def test_rollDie_2():
    result = rollDie('yellow')
    assert isinstance(result, dict)
    assert 'color' in result and 'icon' in result
    assert result['color'] == 'yellow'

def test_rollDie_3():
    result = rollDie('green')
    assert isinstance(result, dict)
    assert 'color' in result and 'icon' in result
    assert result['color'] == 'green'

def test_rollDie_4():
    result = rollDie('red')
    assert result['icon'] in ['shotgun', 'footsteps', 'brains']

def test_rollDie_5():
    result = rollDie('yellow')
    assert result['icon'] in ['shotgun', 'footsteps', 'brains']

def test_rollDie_6():
    result = rollDie('green')
    assert result['icon'] in ['shotgun', 'footsteps', 'brains']

def test_rollDie_7():
    result = rollDie('red')
    if result['icon'] == 'shotgun':
        assert result['color'] in [1, 2, 3]
    elif result['icon'] == 'footsteps':
        assert result['color'] in [4, 5]
    else:
        assert result['color'] == 6

def test_rollDie_8():
    result = rollDie('yellow')
    if result['icon'] == 'shotgun':
        assert result['color'] in [1, 2]
    elif result['icon'] == 'footsteps':
        assert result['color'] in [3, 4]
    else:
        assert result['color'] in [5, 6]

def test_rollDie_9():
    result = rollDie('green')
    if result['icon'] == 'shotgun':
        assert result['color'] == 1
    elif result['icon'] == 'footsteps':
        assert result['color'] in [2, 3]
    else:
        assert result['color'] in [4, 5, 6]

def test_rollDie_10():
    for _ in range(100):
        result = rollDie('red')
        if result['icon'] == 'shotgun':
            assert result['color'] in [1, 2, 3]
        elif result['icon'] == 'footsteps':
            assert result['color'] in [4, 5]
        else:
            assert result['color'] == 6
