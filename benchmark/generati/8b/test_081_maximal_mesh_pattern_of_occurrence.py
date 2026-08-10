from funzione import maximal_mesh_pattern_of_occurrence

def test_maximal_mesh_pattern_of_occurrence_1():
    perm = [1, 2, 3, 4]
    occ = [0, 2]
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}

def test_maximal_mesh_pattern_of_occurrence_2():
    perm = [1, 2, 3, 4]
    occ = [0, 1]
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}

def test_maximal_mesh_pattern_of_occurrence_3():
    perm = [1, 2, 3, 4]
    occ = [0, 1, 2]
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}

def test_maximal_mesh_pattern_of_occurrence_4():
    perm = [1, 2, 3, 4]
    occ = [0, 2, 3]
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}

def test_maximal_mesh_pattern_of_occurrence_5():
    perm = [1, 2, 3, 4]
    occ = [0, 1, 3]
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}

def test_maximal_mesh_pattern_of_occurrence_6():
    perm = [1, 2, 3, 4]
    occ = [0, 2, 1]
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}

def test_maximal_mesh_pattern_of_occurrence_7():
    perm = [1, 2, 3, 4]
    occ = [0, 1, 2, 3]
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2,
