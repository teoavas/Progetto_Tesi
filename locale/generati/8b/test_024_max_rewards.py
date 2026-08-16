from funzione import max_rewards

def test_max_rewards_1():
    actions = ['attack']
    assert max_rewards(actions) == 1

def test_max_rewards_2():
    actions = ['craft: planks', 'attack']
    assert max_rewards(actions) == 3

def test_max_rewards_3():
    actions = ['craft: stick', 'craft: crafting_table', 'attack']
    assert max_rewards(actions) == 11

def test_max_rewards_4():
    actions = ['place: crafting_table', 'nearbyCraft: wooden_pickaxe', 'equip: wooden_pickaxe', 'attack']
    assert max_rewards(actions) == 35

def test_max_rewards_5():
    actions = ['nearbyCraft: stone_pickaxe', 'attack']
    assert max_rewards(actions) == 67

def test_max_rewards_6():
    actions = ['nearbyCraft: furnace', 'equip: stone_pickaxe', 'attack']
    assert max_rewards(actions) == 163
