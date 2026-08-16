from funzione import rollDie

def test_rollDie_1():
    assert rollDie(RED) in ({'color': 'red', 'icon': 'shotgun'}, {'color': 'red', 'icon': 'footsteps'}, {'color': 'red', 'icon': 'brains'})

def test_rollDie_2():
    assert rollDie(YELLOW) in ({'color': 'yellow', 'icon': 'shotgun'}, {'color': 'yellow', 'icon': 'footsteps'}, {'color': 'yellow', 'icon': 'brains'})

def test_rollDie_3():
    assert rollDie(GREEN) in ({'color': 'green', 'icon': 'shotgun'}, {'color': 'green', 'icon': 'footsteps'}, {'color': 'green', 'icon': 'brains'})

def test_rollDie_4():
    assert rollDie(RED) != rollDie(YELLOW)
    assert rollDie(RED) != rollDie(GREEN)

def test_rollDie_5():
    result = rollDie(RED)
    assert 'color' in result
    assert 'icon' in result

def test_rollDie_6():
    result = rollDie(RED)
    assert isinstance(result, dict)

def test_rollDie_7():
    with pytest.raises(TypeError):
        rollDie('invalid_die')
