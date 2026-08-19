import pytest

def test_max_rewards_1():
    assert max_rewards(['attack']) == 1
    assert max_rewards(['attack', 'craft: planks']) == 3
    assert max_rewards(['attack', 'craft: stick', 'place: crafting_table']) == 11
    assert max_rewards(['attack', 'place: crafting_table', 'nearbyCraft: wooden_pickaxe']) == 19
    assert max_rewards(['attack', 'nearbyCraft: stone_pickaxe']) == 67

def test_max_rewards_2():
    assert max_rewards(['craft: planks', 'craft: stick', 'craft: crafting_table']) == 3
    assert max_rewards(['craft: planks', 'craft: stick', 'place: crafting_table', 'nearbyCraft: wooden_pickaxe']) == 19
    assert max_rewards(['craft: planks', 'craft: stick', 'place: crafting_table', 'nearbyCraft: stone_pickaxe', 'equip: wooden_pickaxe']) == 35

def test_max_rewards_3():
    assert max_rewards(['attack', 'craft: stick', 'craft: crafting_table', 'nearbyCraft: wooden_pickaxe']) == 11
    assert max_rewards(['attack', 'place: crafting_table', 'nearbyCraft: stone_pickaxe']) == 67
    assert max_rewards(['attack', 'nearbyCraft: stone_pickaxe', 'equip: stone_pickaxe']) == 99

def test_max_rewards_4():
    assert max_rewards(['craft: stick', 'craft: crafting_table', 'place: crafting_table', 'nearbyCraft: wooden_pickaxe']) == 19
    assert max_rewards(['attack', 'craft: stick', 'craft: crafting_table', 'nearbyCraft: stone_pickaxe']) == 67

def test_max_rewards_5():
    assert max_rewards(['attack', 'place: crafting_table', 'nearbyCraft: stone_pickaxe', 'equip: wooden_pickaxe']) == 35
    assert max_rewards(['attack', 'nearbyCraft: stone_pickaxe', 'equip: stone_pickaxe']) == 99

def test_max_rewards_6():
    assert max_rewards(['craft: stick', 'place: crafting_table', 'nearbyCraft: stone_pickaxe', 'equip: wooden_pickaxe']) == 35
    assert max_rewards(['attack', 'craft: stick', 'craft: crafting_table', 'nearbyCraft: stone_pickaxe']) == 67

def test_max_rewards_7():
    assert max_rewards(['attack', 'place: crafting_table', 'nearbyCraft: stone_pickaxe', 'equip: wooden_pickaxe', 'nearbyCraft: iron_pickaxe']) == 1571
    assert max_rewards(['attack', 'craft: stick', 'craft: crafting_table', 'nearbyCraft: stone_pickaxe', 'equip: wooden_pickaxe']) == 35

def test_max_rewards_8():
    assert max_rewards(['attack', 'place: crafting_table', 'nearbyCraft: iron_pickaxe', 'equip: stone_pickaxe']) == 291
