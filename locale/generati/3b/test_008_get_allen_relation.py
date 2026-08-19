from funzione import get_allen_relation

def test_get_allen_relation_1():
    assert get_allen_relation((10, 20), (30, 40)) == 'meets'

def test_get_allen_relation_2():
    assert get_allen_relation((15, 25), (35, 45)) == 'overlaps'

def test_get_allen_relation_3():
    assert get_allen_relation((5, 10), (20, 30)) == 'after'

def test_get_allen_relation_4():
    assert get_allen_relation((1, 2), (3, 4)) == 'before'

def test_get_allen_relation_5():
    assert get_allen_relation((15, 25), (10, 20)) == 'overlapped_by'

def test_get_allen_relation_6():
    assert get_allen_relation((1, 2), (3, 4)) == 'meets'

def test_get_allen_relation_7():
    assert get_allen_relation((5, 10), (15, 20)) == 'during'
