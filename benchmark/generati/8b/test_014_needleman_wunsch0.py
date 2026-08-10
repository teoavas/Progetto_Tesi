from funzione import needleman_wunsch0

def test_needleman_wunsch0_1():
    A = 'ATCG'
    B = 'ACGT'
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', 'ACGT', 1)

def test_needleman_wunsch0_2():
    A = 'ATCG'
    B = 'ATGC'
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', '_ATGC', 1)

def test_needleman_wunsch0_3():
    A = 'ATCG'
    B = 'ATG'
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', '_ATG', 1)

def test_needleman_wunsch0_4():
    A = 'ATCG'
    B = 'AT'
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', '__AT', 1)

def test_needleman_wunsch0_5():
    A = 'ATCG'
    B = 'ATCG'
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', 'ATCG', 6)

def test_needleman_wunsch0_6():
    A = 'ATCG'
    B = ''
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('ATCG', '', 0)

def test_needleman_wunsch0_7():
    A = ''
    B = 'ATCG'
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('', 'ATCG', 0)

def test_needleman_wunsch0_8():
    A = ''
    B = ''
    mu = -1
    delta = -1
    assert needleman_wunsch0(A, B, mu, delta) == ('', '', 0)
