from funzione import turn_sequence

def test_turn_sequence_1():
    assert turn_sequence(['u', 'r', 'r', 'u', 'l', 'l']) == 'rrll'

def test_turn_sequence_2():
    assert turn_sequence(['d', 'l', 'l', 'd', 'r', 'r']) == 'llrr'

def test_turn_sequence_3():
    assert turn_sequence(['u', 'r', 'l', 'u', 'r', 'l']) == 'rlrl'

def test_turn_sequence_4():
    assert turn_sequence(['d', 'l', 'r', 'd', 'l', 'r']) == 'lrld'

def test_turn_sequence_5():
    assert turn_sequence(['u', 'u', 'u', 'u', 'u', 'u']) == 'ssssss'

def test_turn_sequence_6():
    assert turn_sequence(['d', 'd', 'd', 'd', 'd', 'd']) == 'ssssss'

def test_turn_sequence_7():
    assert turn_sequence(['r', 'r', 'r', 'r', 'r', 'r']) == 'ssssss'

def test_turn_sequence_8():
    assert turn_sequence(['l', 'l', 'l', 'l', 'l', 'l']) == 'ssssss'
