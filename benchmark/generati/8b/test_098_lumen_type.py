from funzione import lumen_type

def test_lumen_type_1():
    lumen_list = [[0, 0], [1, 1], [2, 2]]
    border_set = {0, 1}
    result = lumen_type(lumen_list, border_set)
    assert result == {0: 'ICMmi', 1: 'TEmi', 2: 'ICM'}

def test_lumen_type_2():
    lumen_list = [[0, 0], [1, 1], [2, 2]]
    border_set = {0, 1}
    result = lumen_type(lumen_list, border_set, wild_list=[0])
    assert result == {0: 'TEmi', 1: 'TEmi', 2: 'ICM'}

def test_lumen_type_3():
    lumen_list = [[0, 0], [1, 1], [2, 2]]
    border_set = {0, 1}
    result = lumen_type(lumen_list, border_set, mutants_list=[1])
    assert result == {0: 'ICMmi', 1: 'mutantsmi', 2: 'ICM'}

def test_lumen_type_4():
    lumen_list = [[0, 0], [1, 1], [2, 2]]
    border_set = {0, 1}
    result = lumen_type(lumen_list, border_set, wild_list=[0], mutants_list=[1])
    assert result == {0: 'TEmi', 1: 'wild_mutantsmi', 2: 'ICM'}

def test_lumen_type_5():
    lumen_list = [[0, 0], [1, 1], [2, 2]]
    border_set = {0, 1}
    result = lumen_type(lumen_list, border_set, wild_mutants_list=[1])
    assert result == {0: 'ICMmi', 1: 'wild_mutantsmi', 2: 'ICM'}

def test_lumen_type_6():
    lumen_list = [[0, 0], [1, 1], [2, 2]]
    border_set = {0, 1}
    result = lumen_type(lumen_list, border_set, wild_list=[0], wild_mutants_list=[1])
    assert result == {0: 'TEmi', 1: 'wild_mutantsmi', 2: 'ICM'}

def test_lumen_type_7():
    lumen_list = [[0, 0], [1, 1], [2, 2]]
    border_set = {0, 1}
    result = lumen_type(lumen_list, border_set, topology='chain')
    assert result == {0: 'ICMmi', 1: 'ICMmi', 2: 'ICMmi'}

def test_lumen_type_8():
    lumen_list = [[0, 0], [1, 1], [2, 2]]
    border_set = {0, 1}
    result = lumen_type(lumen_list, border_set, mutants_list=[1], topology='chain')
    assert result == {0: 'ICMmi', 1: 'ICMmi', 2: 'ICMmi'}
