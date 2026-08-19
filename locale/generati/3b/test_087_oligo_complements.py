from funzione import oligo_complements

def test_oligo_complements_1():
    assert oligo_complements("ATCG") == ["ATGC", "TAGC", "GCTA", "GTCA"]

def test_oligo_complements_2():
    assert oligo_complements("UACG") == ["TUGA", "TAUG", "GUAU", "GUAC"]

def test_oligo_complements_3():
    assert oligo_complements("") == []

def test_oligo_complements_4():
    assert oligo_complements("AAAA") == ["TTTT", "TTTT", "TTTT", "TTTT"]

def test_oligo_complements_5():
    assert oligo_complements("ATGC") == ["TAGC", "GCTA", "TCAg", "GTCA"]

def test_oligo_complements_6():
    with pytest.raises(TypeError):
        oligo_complements(123)

def test_oligo_complements_7():
    with pytest.raises(TypeError):
        oligo_complements(None)
