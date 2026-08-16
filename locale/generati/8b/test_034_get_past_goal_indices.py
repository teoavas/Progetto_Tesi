from funzione import get_past_goal_indices

def test_get_past_goal_indices_1():
    current_robot_time_index = 5
    goal_indices = [0, 2, 4]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == [0, 2]

def test_get_past_goal_indices_2():
    current_robot_time_index = 10
    goal_indices = [0, 5, 7, 9]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == [0, 5, 7]

def test_get_past_goal_indices_3():
    current_robot_time_index = 1
    goal_indices = [0, 2, 4]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == []

def test_get_past_goal_indices_4():
    current_robot_time_index = 5
    goal_indices = [0, 3, 6]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == [0]

def test_get_past_goal_indices_5():
    current_robot_time_index = 10
    goal_indices = [0, 2, 4]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == []

def test_get_past_goal_indices_6():
    current_robot_time_index = 15
    goal_indices = [0, 5, 7, 9]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == [0, 5]

def test_get_past_goal_indices_7():
    current_robot_time_index = 20
    goal_indices = [0, 10, 15, 18]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == [0, 10]
