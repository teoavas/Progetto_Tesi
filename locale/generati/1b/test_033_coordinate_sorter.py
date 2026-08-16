import pytest

def test_coordinate_sorter_1():
    assert coordinate_sorter(0, 10, []) == 0

def test_coordinate_sorter_2():
    assert coordinate_sorter(5, 15, [{'coordinates': {'start': 3, 'stop': 7}}]) == 4

def test_coordinate_sorter_3():
    assert coordinate_sorter(8, 18, [{'coordinates': {'start': 1, 'stop': 9}}, {'coordinates': {'start': 11, 'stop': 19}}])

def test_coordinate_sorter_4():
    assert coordinate_sorter(20, 30, [{'coordinates': {'start': 2, 'stop': 10}}, {'coordinates': {'start': 12, 'stop': 22}}])

def test_coordinate_sorter_5():
    assert coordinate_sorter(35, 45, [{'coordinates': {'start': 4, 'stop': 14}}, {'coordinates': {'start': 16, 'stop': 24}}])

def test_coordinate_sorter_6():
    assert coordinate_sorter(50, 60, [{'coordinates': {'start': 5, 'stop': 15}}, {'coordinates': {'start': 17, 'stop': 25}}])

def test_coordinate_sorter_7():
    assert coordinate_sorter(65, 75, [{'coordinates': {'start': 6, 'stop': 16}}, {'coordinates': {'start': 18, 'stop': 26}}])
