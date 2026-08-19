import pytest

def test_change_display_1():
    data = [0, 0, 0, 0, 0]
    change_display(data, 10)
    assert all(isinstance(x, int) for x in data)

def test_change_display_2():
    data = [0, 0, 0, 0, 0]
    change_display(data, 5)
    assert all(isinstance(x, int) for x in data)

def test_change_display_3():
    data = [0, 0, 0, 0, 0]
    change_display(data, 15)
    assert all(isinstance(x, int) for x in data)

def test_change_display_4():
    data = [0, 0, 0, 0, 0]
    change_display(data, 25)
    assert all(isinstance(x, int) for x in data)

def test_change_display_5():
    data = [0, 0, 0, 0, 0]
    change_display(data, 30)
    assert all(isinstance(x, int) for x in data)

def test_change_display_6():
    data = [0, 0, 0, 0, 0]
    change_display(data, 35)
    assert all(isinstance(x, int) for x in data)

def test_change_display_7():
    data = [0, 0, 0, 0, 0]
    change_display(data, 40)
    assert all(isinstance(x, int) for x in data)

def test_change_display_8():
    data = [0, 0, 0, 0, 0]
    change_display(data, 50)
    assert all(isinstance(x, int) for x in data)
