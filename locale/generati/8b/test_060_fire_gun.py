```python
from funzione import fire_gun

def test_fire_gun_1():
    result = fire_gun(100, 200, 5, 3, 2, 1)
    assert result[0] == 110
    assert result[1] == 203
    assert result[2] is True
    assert result[3] is False
    assert result[4] is False

def test_fire_gun_2():
    result = fire_gun(100, 200, 5, 3, 2, 2)
    assert result[0] == 110
    assert result[1] == 203
    assert result[2] is True
    assert result[3] is True
    assert result[4] is False

def test_fire_gun_3():
    result = fire_gun(100, 200, 5, 3, 2, 1)
    assert result[0] == 110
    assert result[1] == 203
    assert result[2] is True
    assert result[3] is False
    assert result[4] is False

def test_fire_gun_4():
    result = fire_gun(100, 200, 5, 3, 10, 1)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[3] is False
    assert result[4] is False

def test_fire_gun_5():
    result = fire_gun(100, 200, 5, 3, 10, 2)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[3] is True
    assert result[4] is False

def test_fire_gun_6():
    result = fire_gun(100, 200, 5, 3, 10, 1)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[3] is False
    assert result[4] is False

def test_fire_gun_7():
    result = fire_gun(100, 200, 5, 3, 10, 2)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[3] is True
    assert result[4] is False

def test_fire_gun_8():
    result = fire_gun(100, 200, 5, 3, 10, 1)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[3] is False
    assert result[4] is False

def test_fire_gun_9():
    result = fire_gun(100, 200, 5, 3, 10, 2)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[3] is True
    assert result[4] is False

def test_fire_gun_10():
    result = fire_gun(100, 200, 5, 3, 10, 1)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[3] is False
    assert result[4] is False

def test_fire_gun_11():
    result = fire_gun(100, 200, 5, 3, 10, 2)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[3] is True
    assert result[4] is False

def test_fire_gun_12():
    result = fire_gun(100, 200, 5, 3, 10, 1)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[3] is False
    assert result[4] is False

def test_fire_gun_13():
    result = fire_gun(100, 200, 5, 3, 10, 2)
    assert result[0] == 550
    assert result[1] == 603
    assert result[2] is True
    assert result[
