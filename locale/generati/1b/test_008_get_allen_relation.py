import pytest

def test_get_allen_relation_1():
    assert get_allen_relation(5, 4) == 'meets'

def test_get_allen_relation_2():
    assert get_allen_relation(3, 6) == 'before'

def test_get_allen_relation_3():
    assert get_allen_relation(7, 8) == 'after'

def test_get_allen_relation_4():
    assert get_allen_relation(1, 5) == 'during'

def test_get_allen_relation_5():
    assert get_allen_relation(2, 6) == 'overlaps'

def test_get_allen_relation_6():
    assert get_allen_relation(3, 7) == 'starts'

def test_get_allen_relation_7():
    assert get_allen_relation(4, 8) == 'finished_by'

def test_get_allen_relation_8():
    assert get_allen_relation(9, 10) == 'overlapped_by'
