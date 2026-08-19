from funzione import fire_gun

def test_fire_gun_1():
    assert fire_gun(0, 0, 0, 0, 10, 1) == (0, 0, False, False, False)

def test_fire_gun_2():
    assert fire_gun(100, 100, 5, 5, 10, 1) == (105, 105, True, False, False)

def test_fire_gun_3():
    assert fire_gun(-100, -100, -5, -5, 10, 1) == (-95, -95, True, False, False)

def test_fire_gun_4():
    assert fire_gun(0, 800, 0, 0, 10, 1) == (0, 800, False, False, False)

def test_fire_gun_5():
    assert fire_gun(100, 0, 0, 0, 10, 2) == (105, 0, True, False, False)

def test_fire_gun_6():
    assert fire_gun(-100, -800, -5, -5, 10, 1) == (-95, -795, True, False, False)

def test_fire_gun_7():
    assert fire_gun(0, 0, 0, 0, 10, 2) == (0, 0, False, False, False)

def test_fire_gun_8():
    assert fire_gun(100, 100, 5, 5, 10, 1) == (105, 105, True, True, False)
