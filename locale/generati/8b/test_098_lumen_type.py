from funzione import lumen_type

def test_lumen_type_1():
    lumen_list = [[0, 0], [1, 2], [3, 4]]
    border_set = {0}
    wild_list = []
    mutants_list = []
    wild_mutants_list = []
    topology = 'hexagonal'
    assert lumen_type(lumen_list, border_set, wild_list, mutants_list, wild_mutants_list, topology) == {'0': 'ICMmi', '1': 'ICMbi', '2': 'ICMbi'}

def test_lumen_type_2():
    lumen_list = [[0, 0], [1, 2], [3, 4]]
    border_set = {0}
    wild_list = []
    mutants_list = []
    wild_mutants_list = []
    topology = 'chain'
    assert lumen_type(lumen_list, border_set, wild_list, mutants_list, wild_mutants_list, topology) == {'0': 'ICMmi', '1': 'ICMmi', '2': 'ICMmi'}

def test_lumen_type_3():
    lumen_list = [[0, 0], [1, 2], [3, 4]]
    border_set = {0}
    wild_list = []
    mutants_list = [0]
    wild_mutants_list = []
    topology = 'hexagonal'
    assert lumen_type(lumen_list, border_set, wild_list, mutants_list, wild_mutants_list, topology) == {'0': 'mutantsmi', '1': 'ICMbi', '2': 'ICMbi'}

def test_lumen_type_4():
    lumen_list = [[0, 0], [1, 2], [3, 4]]
    border_set = {0}
    wild_list = []
    mutants_list = []
    wild_mutants_list = [0]
    topology = 'hexagonal'
    assert lumen_type(lumen_list, border_set, wild_list, mutants_list, wild_mutants_list, topology) == {'0': 'wild_mutantsmi', '1': 'ICMbi', '2': 'ICMbi'}

def test_lumen_type_5():
    lumen_list = [[0, 0], [1, 2], [3, 4]]
    border_set = {0}
    wild_list = []
    mutants_list = []
    wild_mutants_list = []
    topology = 'hexagonal'
    assert lumen_type(lumen_list, border_set, wild_list, mutants_list, wild_mutants_list, topology) == {'0': 'ICMmi', '1': 'ICMbi', '2': 'ICMbi'}

def test_lumen_type_6():
    lumen_list = [[0, 0], [1, 2], [3, 4]]
    border_set = {0}
    wild_list = []
    mutants_list = []
    wild_mutants_list = []
    topology = 'hexagonal'
    assert lumen_type(lumen_list, border_set, wild_list, mutants_list, wild_mutants_list, topology) == {'0': 'ICMmi', '1': 'ICMbi', '2': 'ICMbi'}

def test_lumen_type_7():
    lumen_list = [[0, 0], [1, 2], [3, 4]]
    border_set = {0}
    wild_list = []
    mutants_list = []
    wild_mutants_list = []
    topology = 'hexagonal'
    assert lumen_type(lumen_list, border_set, wild_list, mutants_list, wild_mutants_list, topology) == {'0': 'ICMmi', '1': 'ICMbi', '2': 'ICMbi'}

def test_lumen_type_8():
    lumen_list = [[0, 0], [1, 2], [3, 4]]
    border_set = {0}
    wild_list = []
    mutants_list = []
    wild_mutants_list = []
    topology = 'hexagonal'
    assert lumen_type(lumen_list, border_set, wild_list, mutants_list, wild_mutants_list, topology) == {'0': 'ICMmi', '1': 'ICMbi', '2': 'ICMbi'}
