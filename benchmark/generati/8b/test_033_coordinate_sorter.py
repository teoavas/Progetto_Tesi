from funzione import coordinate_sorter

def test_coordinate_sorter_1():
    assert coordinate_sorter(1, 1, []) == 0

def test_coordinate_sorter_2():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}]) == 0

def test_coordinate_sorter_3():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}, {'coordinates': {'start': 2, 'stop': 2}}]) == 0

def test_coordinate_sorter_4():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}, {'coordinates': {'start': 2, 'stop': 2}}, {'coordinates': {'start': 3, 'stop': 3}}]) == 0

def test_coordinate_sorter_5():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}, {'coordinates': {'start': 2, 'stop': 2}}, {'coordinates': {'start': 3, 'stop': 3}}, {'coordinates': {'start': 4, 'stop': 4}}]) == 0

def test_coordinate_sorter_6():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}, {'coordinates': {'start': 2, 'stop': 2}}, {'coordinates': {'start': 3, 'stop': 3}}, {'coordinates': {'start': 4, 'stop': 4}}, {'coordinates': {'start': 5, 'stop': 5}}]) == 0

def test_coordinate_sorter_7():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}, {'coordinates': {'start': 2, 'stop': 2}}, {'coordinates': {'start': 3, 'stop': 3}}, {'coordinates': {'start': 4, 'stop': 4}}, {'coordinates': {'start': 5, 'stop': 5}}, {'coordinates': {'start': 6, 'stop': 6}}]) == 0

def test_coordinate_sorter_8():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}, {'coordinates': {'start': 2, 'stop': 2}}, {'coordinates': {'start': 3, 'stop': 3}}, {'coordinates': {'start': 4, 'stop': 4}}, {'coordinates': {'start': 5, 'stop': 5}}, {'coordinates': {'start': 6, 'stop': 6}}, {'coordinates': {'start': 7, 'stop': 7}}]) == 0

def test_coordinate_sorter_9():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}, {'coordinates': {'start': 2, 'stop': 2}}, {'coordinates': {'start': 3, 'stop': 3}}, {'coordinates': {'start': 4, 'stop': 4}}, {'coordinates': {'start': 5, 'stop': 5}}, {'coordinates': {'start': 6, 'stop': 6}}, {'coordinates': {'start': 7, 'stop': 7}}, {'coordinates': {'start': 8, 'stop': 8}}]) == 0

def test_coordinate_sorter_10():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}, {'coordinates': {'start': 2, 'stop': 2}}, {'coordinates': {'start': 3, 'stop': 3}}, {'coordinates': {'start': 4, 'stop': 4}}, {'coordinates': {'start': 5, 'stop': 5}}, {'coordinates': {'start': 6, 'stop': 6}}, {'coordinates': {'start': 7, 'stop': 7}}, {'coordinates': {'start': 8, 'stop': 8}}, {'coordinates': {'start': 9, 'stop': 9}}]) == 0

def test_coordinate_sorter_11():
    assert coordinate_sorter(1, 1, [{'coordinates': {'start': 1, 'stop': 1}}, {'coordinates': {'start': 2, 'stop': 2}}, {'coordinates': {'start': 3, 'stop': 3}}, {'coordinates': {'start': 4, 'stop': 4}}, {'coordinates': {'start': 5, 'stop': 5}}, {'coordinates': {'
