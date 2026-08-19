from funzione import needleman_wunsch0

def test_needleman_wunsch0_1():
    A = 'ATCG'
    B = 'ACGT'
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', '_ACGT', 2)

def test_needleman_wunsch0_2():
    A = 'ATCG'
    B = 'GCTA'
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', '_GCTA', 2)

def test_needleman_wunsch0_3():
    A = ''
    B = 'ACGT'
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('', 'ACGT', 4)

def test_needleman_wunsch0_4():
    A = 'ATCG'
    B = ''
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', '', 4)

def test_needleman_wunsch0_5():
    A = 'ATCG'
    B = 'ACGT'
    mu = 2
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', '_ACGT', 3)

def test_needleman_wunsch0_6():
    A = 'ATCG'
    B = 'GCTA'
    mu = 2
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', '_GCTA', 3)

def test_needleman_wunsch0_7():
    A = ''
    B = 'ACGT'
    mu = 2
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('', 'ACGT', 4)
