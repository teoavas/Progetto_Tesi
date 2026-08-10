from funzione import oligo_complements

def test_oligo_complements_1():
    assert oligo_complements('ATCG') == ['ATCG', 'TAGC', 'CGAT', 'TCGA']

def test_oligo_complements_2():
    assert oligo_complements('ATGC') == ['ATGC', 'CAGT', 'CGAT', 'TCGA']

def test_oligo_complements_3():
    assert oligo_complements('AT') == ['AT', 'TA', 'TA', 'AT']

def test_oligo_complements_4():
    assert oligo_complements('A') == ['A', 'T', 'A', 'T']

def test_oligo_complements_5():
    assert oligo_complements('T') == ['T', 'A', 'T', 'A']

def test_oligo_complements_6():
    assert oligo_complements('U') == ['U', 'A', 'U', 'A']

def test_oligo_complements_7():
    assert oligo_complements('C') == ['C', 'G', 'C', 'G']

def test_oligo_complements_8():
    assert oligo_complements('G') == ['G', 'C', 'G', 'C']
