from funzione import locate_alignment

def test_locate_alignment_1():
    assert locate_alignment('ATCG', 'ATGC', 0) == [0]

def test_locate_alignment_2():
    assert locate_alignment('ATCG', 'ATGC', 1, resMatch=True) == []

def test_locate_alignment_3():
    assert locate_alignment('ATCG', 'ATGC', 0, resMatch=False) == [0]

def test_locate_alignment_4():
    assert locate_alignment('ATCG', 'ATGC', 2, resMatch=False) == [2]

def test_locate_alignment_5():
    assert locate_alignment('ATCG', 'ATGC', 3, resMatch=False) == []

def test_locate_alignment_6():
    assert locate_alignment('ATCG', 'ATGC', 0, resMatch=True) == [0]

def test_locate_alignment_7():
    assert locate_alignment('ATCG', 'ATGC', 1, resMatch=True) == []

def test_locate_alignment_8():
    assert locate_alignment('ATCG', 'ATGC', 2, resMatch=True) == []
