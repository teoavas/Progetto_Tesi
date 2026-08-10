from funzione import get_allen_relation

def test_get_allen_relation_1():
    assert get_allen_relation((1, 2), (3, 4)) == 'before'

def test_get_allen_relation_2():
    assert get_allen_relation((1, 2), (2, 3)) == 'overlaps'

def test_get_allen_relation_3():
    assert get_allen_relation((1, 2), (1, 2)) == 'equal'

def test_get_allen_relation_4():
    assert get_allen_relation((1, 2), (2, 1)) == 'after'

def test_get_allen_relation_5():
    assert get_allen_relation((1, 2), (1, 3)) == 'during'

def test_get_allen_relation_6():
    assert get_allen_relation((1, 2), (1, 1)) == 'starts'

def test_get_allen_relation_7():
    assert get_allen_relation((1, 2), (2, 2)) == 'finishes'
