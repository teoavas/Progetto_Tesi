```python
import pytest

def test_turn_sequence_1():
    assert turn_sequence([0, 1]) == "s"
    assert turn_sequence([1, 2]) == "l"
    assert turn_sequence([-1, -2]) == "r"

def test_turn_sequence_2():
    assert turn_sequence([0, 1, 2]) == "sll"
    assert turn_sequence([1, 2, 3]) == "rrll"
    assert turn_sequence([2, 3, 4]) == "lrrrl"

def test_turn_sequence_3():
    assert turn_sequence([-1, -2, -3]) == "rlllr"
    assert turn_sequence([-2, -3, -4]) == "rrllr"
    assert turn_sequence([-3, -4, -5]) == "lllrrr"

def test_turn_sequence_4():
    assert turn_sequence([0, 1, 2, 3]) == "sllll"
    assert turn_sequence([1, 2, 3, 4]) == "rlrrll"
    assert turn_sequence([2, 3, 4, 5]) == "lrrrllr"

def test_turn_sequence_5():
    assert turn_sequence([-1, -2, -3, -4]) == "rrllll"
    assert turn_sequence([-2, -3, -4, -5]) == "rrrrrlr"
    assert turn_sequence([-3, -4, -5, -6]) == "lllrrrr"

def test_turn_sequence_6():
    assert turn_sequence([0, 1, 2, 3, 4]) == "sllllll"
    assert turn_sequence([1, 2, 3, 4, 5]) == "rlrrrrr"
    assert turn_sequence([2, 3, 4, 5, 6]) == "lrrrrrr"

def test_turn_sequence_7():
    assert turn_sequence([-1, -2, -3, -4, -5]) == "rrllllll"
    assert turn_sequence([-2, -3, -4, -5, -6]) == "rrrrrlrll"
    assert turn_sequence([-3, -4, -5, -6, -7]) == "lllrrrrrr"

def test_turn_sequence_8():
    assert turn_sequence([0, 1, 2, 3, 4, 5]) == "sllllllll"
    assert turn_sequence([1, 2, 3, 4, 5, 6]) == "rlrrrrrrrll"
    assert turn_sequence([2, 3, 4, 5, 6, 7]) == "lrrrrrrrrrr"
