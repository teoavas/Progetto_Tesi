test_needleman_wunsch0_1
def test_needleman_wunsch0_2():
    A = ['ATCG', 'TGCA']
    B = ['TACG', 'GCTA']
    mu, delta = -1, -1
    result = needleman_wunsch0(A, B, mu, delta)
    assert result == ('TAGC', 'TCGA', [delta*2, 3])

test_needleman_wunsch0_3
def test_needleman_wunsch0_4():
    A = ['ATCG', 'TGCA']
    B = ['TACG', 'GCTA']
    mu, delta = -1, 1
    result = needleman_wunsch0(A, B, mu, delta)
    assert result == ('TAGC', 'TCGA', [delta*2, 3])

test_needleman_wunsch0_5
def test_needleman_wunsch0_6():
    A = ['ATCG', 'TGCA']
    B = ['TACG', 'GCTA']
    mu, delta = -1, -1
    result = needleman_wunsch0(A, B, mu, delta)
    assert result == ('TAGC', 'TCGA', [delta*2, 3])

test_needleman_wunsch0_7
def test_needleman_wunsch0_8():
    A = ['ATCG', 'TGCA']
    B = ['TACG', 'GCTA']
    mu, delta = -1, 1
    result = needleman_wunsch0(A, B, mu, delta)
    assert result == ('TAGC', 'TCGA', [delta*2, 3])

test_needleman_wunsch0_9
def test_needleman_wunsch0_10():
    A = ['ATCG', 'TGCA']
    B = ['TACG', 'GCTA']
    mu, delta = -1, -1
    result = needleman_wunsch0(A, B, mu, delta)
    assert result == ('TAGC', 'TCGA', [delta*2, 3])
