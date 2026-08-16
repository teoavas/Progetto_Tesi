import pytest

@pytest.fixture
def player():
    return 1

def test_fire_gun_1():
    x = 100
    y = 200
    xvel = 5
    yvel = 3
    time_passed_seconds = 2
    result = fire_gun(x, y, xvel, yvel, time_passed_seconds, player)
    assert result[0] == 100
    assert result[1] == False
    assert not result[2]
    assert not result[3]

def test_fire_gun_2():
    x = 500
    y = 300
    xvel = -5
    yvel = -3
    time_passed_seconds = 4
    result = fire_gun(x, y, xvel, yvel, time_passed_seconds, player)
    assert result[0] == 500
    assert result[1] == False
    assert not result[2]
    assert not result[3]

def test_fire_gun_3():
    x = 200
    y = 400
    xvel = -10
    yvel = -8
    time_passed_seconds = 6
    result = fire_gun(x, y, xvel, yvel, time_passed_seconds, player)
    assert result[0] == 190
    assert result[1] == False
    assert not result[2]
    assert not result[3]

def test_fire_gun_4():
    x = 100
    y = 200
    xvel = -5
    yvel = -8
    time_passed_seconds = 6
    result = fire_gun(x, y, xvel, yvel, time_passed_seconds, player)
    assert result[0] == 95
    assert result[1] == False
    assert not result[2]
    assert not result[3]

def test_fire_gun_5():
    x = 500
    y = 300
    xvel = -10
    yvel = -8
    time_passed_seconds = 6
    result = fire_gun(x, y, xvel, yvel, time_passed_seconds, player)
    assert result[0] == 490
    assert result[1] == False
    assert not result[2]
    assert not result[3]

def test_fire_gun_6():
    x = 200
    y = 400
    xvel = -5
    yvel = -8
    time_passed_seconds = 6
    result = fire_gun(x, y, xvel, yvel, time_passed_seconds, player)
    assert result[0] == 195
    assert result[1] == False
    assert not result[2]
    assert not result[3]

def test_fire_gun_7():
    x = 100
    y = 200
    xvel = -10
    yvel = -8
    time_passed_seconds = 6
    result = fire_gun(x, y, xvel, yvel, time_passed_seconds, player)
    assert result[0] == 85
    assert result[1] == False
    assert not result[2]
    assert not result[3]

def test_fire_gun_8():
    x = 500
    y = 300
    xvel = -5
    yvel = -10
    time_passed_seconds = 6
    result = fire_gun(x, y, xvel, yvel, time_passed_seconds, player)
    assert result[0] == 485
    assert result[1] == False
    assert not result[2]
    assert not result[3]
