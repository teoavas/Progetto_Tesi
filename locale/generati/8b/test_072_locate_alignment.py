from funzione import locate_alignment

def test_locate_alignment_1():
    Qseq = "ATCG"
    Sseq = "ATGC-"
    Qstart = 0
    resMatch = False
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == [0]

def test_locate_alignment_2():
    Qseq = "ATCG"
    Sseq = "ATGC-"
    Qstart = 1
    resMatch = False
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == [1]

def test_locate_alignment_3():
    Qseq = "ATCG--"
    Sseq = "ATGC-"
    Qstart = 0
    resMatch = False
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == []

def test_locate_alignment_4():
    Qseq = "ATCG"
    Sseq = "ATGC--"
    Qstart = 0
    resMatch = False
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == [0]

def test_locate_alignment_5():
    Qseq = "ATCG"
    Sseq = "ATGC-"
    Qstart = 0
    resMatch = True
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == []

def test_locate_alignment_6():
    Qseq = "ATCG--"
    Sseq = "ATGC-"
    Qstart = 0
    resMatch = False
    assert locate_alignment(Qseq, Sseq, Qstart, resMatch) == []
