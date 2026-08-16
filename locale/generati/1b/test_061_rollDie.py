import pytest
from funzione import rollDie

def test_rollDie_1():
    assert rollDie(2) == {'COLOR': RED, 'ICON': SHOTGUN}

def test_rollDie_2():
    assert rollDie(3) == {'COLOR': YELLOW, 'ICON': FOOTSTEPS}

def test_rollDie_3():
    assert rollDie(4) == {'COLOR': GREEN, 'ICON': BRAINS}

def test_rollDie_4():
    assert rollDie(5) == {'COLOR': RED, 'ICON': SHOTGUN}

def test_rollDie_5():
    assert rollDie(6) == {'COLOR': YELLOW, 'ICON': FOOTSTEPS}

def test_rollDie_6():
    assert rollDie(1) == {'COLOR': GREEN, 'ICON': SHOTGUN}
