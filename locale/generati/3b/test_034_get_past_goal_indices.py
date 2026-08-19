from funzione import get_past_goal_indices

def test_get_past_goal_indices_1():
    assert get_past_goal_indices(10, [5, 7, 3]) == [5, 7]

def test_get_past_goal_indices_2():
    assert get_past_goal_indices(0, []) == []

def test_get_past_goal_indices_3():
    assert get_past_goal_indices(1, [1]) == [1]

def test_get_past_goal_indices_4():
    assert get_past_goal_indices(5, [10, 15, 20]) == [10, 15, 20]

def test_get_past_goal_indices_5():
    assert get_past_goal_indices(2, [0, 1, 2]) == [0, 1]

def test_get_past_goal_indices_6():
    assert get_past_goal_indices(3, [4, 5, 6]) == []

def test_get_past_goal_indices_7():
    with pytest.raises(ValueError):
        get_past_goal_indices(-1, [10, 15, 20])
