from funzione import calculate_circular_pile_set_positions

def test_calculate_circular_pile_set_positions_1():
    starting_mat_center = (0, 0)
    pile_offset = (1, 1)
    piles_per_side = (5, 5)
    player_index = 1
    n_player = 10
    pile_position_offset = 0
    self_player_index = 0
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 self_player_index, counterclockwise) == (1, 1)

def test_calculate_circular_pile_set_positions_2():
    starting_mat_center = (0, 0)
    pile_offset = (1, 1)
    piles_per_side = (5, 5)
    player_index = 1
    n_player = 10
    pile_position_offset = 0
    self_player_index = 0
    counterclockwise = False
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 self_player_index, counterclockwise) == (0, 1)

def test_calculate_circular_pile_set_positions_3():
    starting_mat_center = (0, 0)
    pile_offset = (1, 1)
    piles_per_side = (5, 5)
    player_index = 1
    n_player = 10
    pile_position_offset = 0
    self_player_index = 0
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 self_player_index, counterclockwise) != (0, 0)

def test_calculate_circular_pile_set_positions_4():
    starting_mat_center = (0, 0)
    pile_offset = (1, 1)
    piles_per_side = (5, 5)
    player_index = 1
    n_player = 10
    pile_position_offset = 0
    self_player_index = 0
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 self_player_index, counterclockwise) == (1, 1)

def test_calculate_circular_pile_set_positions_5():
    starting_mat_center = (0, 0)
    pile_offset = (1, 1)
    piles_per_side = (5, 5)
    player_index = 1
    n_player = 10
    pile_position_offset = 0
    self_player_index = 0
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 self_player_index, counterclockwise) != (0, 0)

def test_calculate_circular_pile_set_positions_6():
    starting_mat_center = (0, 0)
    pile_offset = (1, 1)
    piles_per_side = (5, 5)
    player_index = 1
    n_player = 10
    pile_position_offset = 0
    self_player_index = 0
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 self_player_index, counterclockwise) == (1, 1)

def test_calculate_circular_pile_set_positions_7():
    starting_mat_center = (0, 0)
    pile_offset = (1, 1)
    piles_per_side = (5, 5)
    player_index = 1
    n_player = 10
    pile_position_offset = 0
    self_player_index = 0
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 self_player_index, counterclockwise) != (0, 0)
