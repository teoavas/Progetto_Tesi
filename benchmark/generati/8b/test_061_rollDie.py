import pytest
from funzione import rollDie

def test_rollDie_1():
    assert rollDie('red') == {'color': 'red', 'icon': 'shotgun'}

def test_rollDie_2():
    assert rollDie('red') == {'color': 'red', 'icon': 'footsteps'} or {'color': 'red', 'icon': 'brains'}

def test_rollDie_3():
    assert rollDie('yellow') == {'color': 'yellow', 'icon': 'shotgun'}

def test_rollDie_4():
    assert rollDie('yellow') == {'color': 'yellow', 'icon': 'footsteps'} or {'color': 'yellow', 'icon': 'brains'}

def test_rollDie_5():
    assert rollDie('green') == {'color': 'green', 'icon': 'shotgun'}

def test_rollDie_6():
    assert rollDie('green') == {'color': 'green', 'icon': 'footsteps'} or {'color': 'green', 'icon': 'brains'}

def test_rollDie_7():
    assert rollDie('red') == {'color': 'red', 'icon': 'shotgun'} or {'color': 'red', 'icon': 'footsteps'} or {'color': 'red', 'icon': 'brains'}

def test_rollDie_8():
    assert rollDie('yellow') == {'color': 'yellow', 'icon': 'shotgun'} or {'color': 'yellow', 'icon': 'footsteps'} or {'color': 'yellow', 'icon': 'brains'}

def test_rollDie_9():
    assert rollDie('green') == {'color': 'green', 'icon': 'shotgun'} or {'color': 'green', 'icon': 'footsteps'} or {'color': 'green', 'icon': 'brains'}
