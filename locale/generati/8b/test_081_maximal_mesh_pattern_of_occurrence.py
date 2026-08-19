from funzione import maximal_mesh_pattern_of_occurrence

def test_maximal_mesh_pattern_of_occurrence_1():
    perm = [1, 2, 3]
    occ = {0}
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2)}

def test_maximal_mesh_pattern_of_occurrence_2():
    perm = [1, 2, 3]
    occ = {0, 1}
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (1, 0), (1, 1)}

def test_maximal_mesh_pattern_of_occurrence_3():
    perm = [1, 2, 3]
    occ = {0}
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2)}

def test_maximal_mesh_pattern_of_occurrence_4():
    perm = [1, 2, 3]
    occ = set()
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)}

def test_maximal_mesh_pattern_of_occurrence_5():
    perm = [1, 2, 3]
    occ = {0, 1}
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (1, 0), (1, 1)}

def test_maximal_mesh_pattern_of_occurrence_6():
    perm = [1, 2, 3]
    occ = {0}
    assert maximal_mesh_pattern_of_occurrence(perm, occ) == {(0, 0), (0, 1), (0, 2)}
