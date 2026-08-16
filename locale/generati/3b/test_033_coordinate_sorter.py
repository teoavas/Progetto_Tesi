from funzione import coordinate_sorter

def test_coordinate_sorter_1():
    assert coordinate_sorter(10, 20, [{'coordinates': {'start': 'a', 'stop': 'b'}}]) == 0

def test_coordinate_sorter_2():
    assert coordinate_sorter(15, 25, [{'coordinates': {'start': 'c', 'stop': 'd'}}]) == 1

def test_coordinate_sorter_3():
    assert coordinate_sorter(10, 20, [{'coordinates': {'start': 'e', 'stop': 'f'}}, {'coordinates': {'start': 'g', 'stop': 'h'}}]) == 0

def test_coordinate_sorter_4():
    assert coordinate_sorter(15, 25, [{'coordinates': {'start': 'i', 'stop': 'j'}}]) == 1

def test_coordinate_sorter_5():
    assert coordinate_sorter(10, 20, []) == 0

def test_coordinate_sorter_6():
    assert coordinate_sorter(15, 25, [{'coordinates': {'start': 'k', 'stop': 'l'}}, {'coordinates': {'start': 'm', 'stop': 'n'}}]) == 1

def test_coordinate_sorter_7():
    assert coordinate_sorter(10, 20, [{'coordinates': {'start': 'o', 'stop': 'p'}}]) == 0
