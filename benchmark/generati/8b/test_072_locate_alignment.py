from funzione import locate_alignment

def test_locate_alignment_1():
    Qseq = 'ATCG'
    Sseq = 'ATCG'
    Qstart = 0
    assert locate_alignment(Qseq, Sseq, Qstart) == [0, 1, 2, 3]

def test_locate_alignment_2():
    Qseq = 'ATCG'
    Sseq = 'ATCG-'
    Qstart = 0
    assert locate_alignment(Qseq, Sseq, Qstart) == [0, 1, 2, 3]

def test_locate_alignment_3():
    Qseq = 'ATCG'
    Sseq = 'AT--'
    Qstart = 0
    assert locate_alignment(Qseq, Sseq, Qstart) == [0, 1, 2, 3]

def test_locate_alignment_4():
    Qseq = 'ATCG'
    Sseq = 'ATCG'
    Qstart = 5
    assert locate_alignment(Qseq, Sseq, Qstart) == [5, 6, 7, 8]

def test_locate_alignment_5():
    Qseq = 'ATCG'
    Sseq = 'ATCG'
    Qstart = 0
    resMatch = True
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == [0, 1, 2, 3]

def test_locate_alignment_6():
    Qseq = 'ATCG'
    Sseq = 'ATCG'
    Qstart = 0
    resMatch = True
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == [0, 1, 2, 3]

def test_locate_alignment_7():
    Qseq = 'ATCG'
    Sseq = 'ATCG'
    Qstart = 0
    resMatch = False
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == [0, 1, 2, 3]

def test_locate_alignment_8():
    Qseq = 'ATCG'
    Sseq = 'ATCG'
    Qstart = 0
    resMatch = False
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == [0, 1, 2, 3]
