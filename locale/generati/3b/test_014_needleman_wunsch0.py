from funzione import needleman_wunsch0

def test_needleman_wunsch0_1():
    A = 'ATCG'
    B = 'ACGT'
    assert needleman_wunsch0(A, B) == ('ATCG', 'ACGT', 0)

def test_needleman_wunsch0_2():
    A = 'ATCG'
    B = 'ACGTG'
    assert needleman_wunsch0(A, B) == ('ATCG_', 'ACGTG', -1)

def test_needleman_wunsch0_3():
    A = 'ATCG'
    B = ''
    assert needleman_wunsch0(A, B) == ('ATCG', '', 0)

def test_needleman_wunsch0_4():
    A = ''
    B = 'ACGTG'
    assert needleman_wunsch0(A, B) == ('', 'ACGTG', -1)

def test_needleman_wunsch0_5():
    A = 'ATCG'
    B = 'ACGTG'
    mu = 2
    delta = 3
    assert needleman_wunsch0(A, B, mu=mu, delta=delta) == ('ATCG', 'ACGTG', -1)

def test_needleman_wunsch0_6():
    A = ['A', 'T', 'C', 'G']
    B = ['A', 'C', 'G', 'T']
    assert needleman_wunsch0(A, B) == ('A_A_T_C_G', 'A_A_C_G_T', 0)

def test_needleman_wunsch0_7():
    A = ['ATCG', 'ATCG']
    B = ['ACGT', 'ACGTG']
    assert needleman_wunsch0(A, B) == ('ATCG_ATCG', 'ACGT_ACGTG', -1)
