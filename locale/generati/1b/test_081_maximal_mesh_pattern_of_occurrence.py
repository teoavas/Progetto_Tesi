import pytest

def test_maximal_mesh_pattern_of_occurrence_1():
    assert maximal_mesh_pattern_of_occurrence([0, 2], [0]) == {(0, 0), (0, 1)}

def test_maximal_mesh_pattern_of_occurrence_2():
    assert maximal_mesh_pattern_of_occurrence([1, 3], [1]) == {(1, 1), (1, 2)}

def test_maximal_mesh_pattern_of_occurrence_3():
    assert maximal_mesh_pattern_of_occurrence([0, 1, 2], [0, 1]) == {(0, 0), (0, 1), (1, 0), (1, 1)}

def test_maximal_mesh_pattern_of_occurrence_4():
    assert maximal_mesh_pattern_of_occurrence([0, 3, 6], [0, 2, 3]) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}

def test_maximal_mesh_pattern_of_occurrence_5():
    assert maximal_mesh_pattern_of_occurrence([1, 2], [1, 2]) == {(1, 1), (1, 2), (2, 1), (2, 2)}

def test_maximal_mesh_pattern_of_occurrence_6():
    assert maximal_mesh_pattern_of_occurrence([0, 3, 5], [0, 4]) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}

def test_maximal_mesh_pattern_of_occurrence_7():
    assert maximal_mesh_pattern_of_occurrence([1, 2, 3], [1, 2]) == {(1, 1), (1, 2), (2, 1), (2, 2)}

def test_maximal_mesh_pattern_of_occurrence_8():
    assert maximal_mesh_pattern_of_occurrence([0, 4, 7], [0, 3, 6]) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}
