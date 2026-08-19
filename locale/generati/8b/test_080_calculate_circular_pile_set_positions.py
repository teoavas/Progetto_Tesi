```python
from funzione import calculate_circular_pile_set_positions

def test_calculate_circular_pile_set_positions_1():
    starting_mat_center = (0, 0)
    pile_offset = (10, 20)
    piles_per_side = (-1, -1)
    player_index = 2
    n_player = 5
    pile_position_offset = Pile_Position_Offset.NO_OFFSET
    self_player_index = None
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 starting_index_type=None, self_player_index=self_player_index,
                                                 counterclockwise=counterclockwise) == (10, 40)

def test_calculate_circular_pile_set_positions_2():
    starting_mat_center = (0, 0)
    pile_offset = (10, 20)
    piles_per_side = (-1, -1)
    player_index = 3
    n_player = 5
    pile_position_offset = Pile_Position_Offset.NO_OFFSET
    self_player_index = None
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 starting_index_type=None, self_player_index=self_player_index,
                                                 counterclockwise=counterclockwise) == (20, 40)

def test_calculate_circular_pile_set_positions_3():
    starting_mat_center = (0, 0)
    pile_offset = (10, 20)
    piles_per_side = (-1, -1)
    player_index = 4
    n_player = 5
    pile_position_offset = Pile_Position_Offset.NO_OFFSET
    self_player_index = None
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 starting_index_type=None, self_player_index=self_player_index,
                                                 counterclockwise=counterclockwise) == (0, 60)

def test_calculate_circular_pile_set_positions_4():
    starting_mat_center = (0, 0)
    pile_offset = (10, 20)
    piles_per_side = (-1, -1)
    player_index = 2
    n_player = 5
    pile_position_offset = Pile_Position_Offset.NO_OFFSET
    self_player_index = None
    counterclockwise = False
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 starting_index_type=None, self_player_index=self_player_index,
                                                 counterclockwise=counterclockwise) == (10, 0)

def test_calculate_circular_pile_set_positions_5():
    starting_mat_center = (0, 0)
    pile_offset = (10, 20)
    piles_per_side = (-1, -1)
    player_index = 3
    n_player = 5
    pile_position_offset = Pile_Position_Offset.NO_OFFSET
    self_player_index = None
    counterclockwise = False
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 starting_index_type=None, self_player_index=self_player_index,
                                                 counterclockwise=counterclockwise) == (20, 0)

def test_calculate_circular_pile_set_positions_6():
    starting_mat_center = (0, 0)
    pile_offset = (10, 20)
    piles_per_side = (-1, -1)
    player_index = 4
    n_player = 5
    pile_position_offset = Pile_Position_Offset.NO_OFFSET
    self_player_index = None
    counterclockwise = False
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 starting_index_type=None, self_player_index=self_player_index,
                                                 counterclockwise=counterclockwise) == (0, 20)

def test_calculate_circular_pile_set_positions_7():
    starting_mat_center = (10, 10)
    pile_offset = (1, 2)
    piles_per_side = (-1, -1)
    player_index = 2
    n_player = 5
    pile_position_offset = Pile_Position_Offset.NO_OFFSET
    self_player_index = None
    counterclockwise = True
    assert calculate_circular_pile_set_positions(starting_mat_center, pile_offset, piles_per_side,
                                                 player_index, n_player, pile_position_offset,
                                                 starting_index
