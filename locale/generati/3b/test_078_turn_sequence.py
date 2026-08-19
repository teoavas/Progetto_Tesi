from funzione import turn_sequence

def test_turn_sequence_1():
    assert turn_sequence([0, 0]) == ""

def test_turn_sequence_2():
    assert turn_sequence([0, 1]) == "r"

def test_turn_sequence_3():
    assert turn_sequence([1, 0]) == "l"

def test_turn_sequence_4():
    assert turn_sequence([0, -1]) == "s"

def test_turn_sequence_5():
    assert turn_sequence([-1, 0]) == "s"

def test_turn_sequence_6():
    assert turn_sequence([0, 1, 0]) == ""

def test_turn_sequence_7():
    assert turn_sequence([0, 1, 1]) == "r"
