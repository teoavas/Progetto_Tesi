from funzione import maximal_mesh_pattern_of_occurrence

def test_maximal_mesh_pattern_of_occurrence_1():
    assert len(maximal_mesh_pattern_of_occurrence([1, 2, 3], [0, 1])) == 4

def test_maximal_mesh_pattern_of_occurrence_2():
    assert set(maximal_mesh_pattern_of_occurrence([1, 2, 3], [0, 1])) == {(0, 0), (0, 1), (1, 0), (1, 1)}

def test_maximal_mesh_pattern_of_occurrence_3():
    assert maximal_mesh_pattern_of_occurrence([1, 1, 1], [0]) == set()

def test_maximal_mesh_pattern_of_occurrence_4():
    assert len(maximal_mesh_pattern_of_occurrence([2, 2, 2], [0, 1])) == 9

def test_maximal_mesh_pattern_of_occurrence_5():
    assert maximal_mesh_pattern_of_occurrence([1, 2, 3, 4], [0, 1, 2]) == set()

def test_maximal_mesh_pattern_of_occurrence_6():
    assert len(maximal_mesh_pattern_of_occurrence([1, 1, 1, 1], [0, 1])) == 8

def test_maximal_mesh_pattern_of_occurrence_7():
    assert maximal_mesh_pattern_of_occurrence([2, 3, 4, 5], [0]) == set()
