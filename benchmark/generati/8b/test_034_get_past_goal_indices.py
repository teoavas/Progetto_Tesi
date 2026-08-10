from funzione import get_past_goal_indices

def test_get_past_goal_indices_1():
    current_robot_time_index = 5
    goal_indices = [1, 2, 3, 4, 5]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == [1, 2, 3, 4]

def test_get_past_goal_indices_2():
    current_robot_time_index = 10
    goal_indices = [1, 2, 3, 4, 5]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == [1, 2, 3, 4, 5]

def test_get_past_goal_indices_3():
    current_robot_time_index = 5
    goal_indices = [1, 2, 3, 4]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == [1, 2, 3, 4]

def test_get_past_goal_indices_4():
    current_robot_time_index = 5
    goal_indices = [1, 2, 3, 4, 5, 6]
    result = get_past_goal_indices(current_robot_time_index, goal_indices)
    assert result == [1, 2, 3, 4]

def test_get_past_goal_indices_5():
    current_robot_time_index = 5
    goal_indices = [1, 2, 3, 4, 5]
    result = get_past_goal_indices(current_robot_time_index, goal_indices, filename='test_file')
    assert result == [1, 2, 3, 4]

def test_get_past_goal_indices_6():
    current_robot_time_index = 5
    goal_indices = [1, 2, 3, 4, 5]
    result = get_past_goal_indices(current_robot_time_index, goal_indices, verbose=1)
    assert result == [1, 2, 3, 4]

def test_get_past_goal_indices_7():
    current_robot_time_index = 5
    goal_indices = [1, 2, 3, 4, 5]
    result = get_past_goal_indices(current_robot_time_index, goal_indices, verbose=2)
    assert result == [1, 2, 3, 4]
