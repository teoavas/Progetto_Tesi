import pytest

def test_oligo_complements_1():
    assert oligo_complements("ATCG") == ["TGCA", "ACGT", "GCTA", "CAGT"]

def test_oligo_complements_2():
    assert oligo_complements("TTAA") == ["AAA", "TTTA", "TTCC", "TTGG"]

def test_oligo_complements_3():
    assert oligo_complements("CGTU") == ["UATG", "UGTC", "TCAU", "TAGC"]

def test_oligo_complements_4():
    assert oligo_complements("ACGTU") == ["TGCA", "ACGU", "GCAT", "CTAG"]

def test_oligo_complements_5():
    assert oligo_complements("GCTA") == ["TGA", "TAGC", "CGTA", "ACTG"]

def test_oligo_complements_6():
    assert oligo_complements("UACG") == ["GCA", "UGAC", "AGCU", "CUGA"]

def test_oligo_complements_7():
    assert oligo_complements("TATG") == ["TAGT", "TATT", "TTAG", "TTAT"]
