from funzione import get_allen_relation

def test_get_allen_relation_1():
    assert get_allen_relation((0, 10), (5, 15)) == 'overlaps'

def test_get_allen_relation_2():
    assert get_allen_relation((0, 10), (20, 30)) == 'before'

def test_get_allen_relation_3():
    assert get_allen_relation((0, 10), (0, 10)) == 'equal'

def test_get_allen_relation_4():
    assert get_allen_relation((5, 15), (0, 10)) == 'during'

def test_get_allen_relation_5():
    assert get_allen_relation((0, 10), (0, 20)) == 'contains'

def test_get_allen_relation_6():
    assert get_allen_relation((0, 10), (15, 25)) == 'after'

def test_get_allen_relation_7():
    assert get_allen_relation((5, 15), (5, 15)) == 'starts'
