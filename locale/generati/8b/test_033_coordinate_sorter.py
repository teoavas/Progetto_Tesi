from funzione import coordinate_sorter

def test_coordinate_sorter_1():
    assert coordinate_sorter(10, 20, [{'coordinates': {'start': 5, 'stop': 15}}, {'coordinates': {'start': 16, 'stop': 25}}]) == 0

def test_coordinate_sorter_2():
    assert coordinate_sorter(15, 20, [{'coordinates': {'start': 10, 'stop': 18}}, {'coordinates': {'start': 19, 'stop': 30}}]) == 1

def test_coordinate_sorter_3():
    assert coordinate_sorter(25, 30, [{'coordinates': {'start': 5, 'stop': 15}}, {'coordinates': {'start': 16, 'stop': 25}}]) == 2

def test_coordinate_sorter_4():
    assert coordinate_sorter(10, 10, [{'coordinates': {'start': 5, 'stop': 15}}, {'coordinates': {'start': 16, 'stop': 25}}]) == 0

def test_coordinate_sorter_5():
    assert coordinate_sorter(20, 30, []) == 0

def test_coordinate_sorter_6():
    assert coordinate_sorter(10, 20, [{'coordinates': {'start': 15, 'stop': 18}}, {'coordinates': {'start': 19, 'stop': 25}}]) == 1
