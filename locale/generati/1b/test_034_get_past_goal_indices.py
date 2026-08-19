import pytest
from funzione import get_past_goal_indices

def test_get_past_goal_indices_1():
    assert len(get_past_goal_indices(10, [0, 1, 2], 'test.txt', verbose=1)) == 3

def test_get_past_goal_indices_2():
    assert get_past_goal_indices(15, [0, 1, 2], 'test.txt', verbose=1) == []

def test_get_past_goal_indices_3():
    assert len(get_past_goal_indices(20, [0, 1, 2], 'test.txt', verbose=1)) == 4

def test_get_past_goal_indices_4():
    with pytest.raises(ValueError):
        get_past_goal_indices(25, [0, 1, 2])

def test_get_past_goal_indices_5():
    assert len(get_past_goal_indices(30, [0, 1])) == 2

def test_get_past_goal_indices_6():
    assert get_past_goal_indices(35, []) == []

def test_get_past_goal_indices_7():
    with pytest.raises(ValueError):
        get_past_goal_indices(40, [])

def test_get_past_goal_indices_8():
    assert len(get_past_goal_indices(45, [0])) == 1
