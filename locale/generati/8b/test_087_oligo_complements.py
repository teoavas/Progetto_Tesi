from funzione import oligo_complements

def test_oligo_complements_1():
    assert oligo_complements("ATCG") == ["TAGC", "ATGC", "CGAT", "TCGA"]

def test_oligo_complements_2():
    assert oligo_complements("GCTA") == ["AGCA", "GCTA", "ATGC", "ACGT"]

def test_oligo_complements_3():
    assert oligo_complements("UUUU") == ["TTTT", "UUUU", "UUUU", "TTTT"]

def test_oligo_complements_4():
    assert oligo_complements("AAAA") == ["TTTT", "AAAA", "TTTT", "TTTT"]

def test_oligo_complements_5():
    assert oligo_complements("") == ["", "", "", ""]

def test_oligo_complements_6():
    assert oligo_complements("ATGC") == ["TAGC", "ATGC", "CGAT", "TCGA"]
