from funzione import max_rewards

def test_max_rewards_1():
    assert max_rewards(['attack']) == 1

def test_max_rewards_2():
    assert max_rewards(['craft: planks']) == 3

def test_max_rewards_3():
    assert max_rewards(['craft: stick', 'craft: crafting_table']) == 11

def test_max_rewards_4():
    assert max_rewards(['place: crafting_table', 'nearbyCraft: wooden_pickaxe']) == 19

def test_max_rewards_5():
    assert max_rewards(['nearbyCraft: stone_pickaxe']) == 67

def test_max_rewards_6():
    assert max_rewards(['equip: stone_pickaxe', 'nearbyCraft: furnace']) == 163

def test_max_rewards_7():
    assert max_rewards(['place: furnace', 'nearbySmelt: iron_ingot']) == 291
