import pytest
from funzione import uniformate2

@pytest.mark.parametrize("word", ["FATHA", "DAMMA", "KASRA", "SUKUN"])
def test_uniformate2_1(word):
    assert uniformate2(word) in (word, "NOT_DEF_HARAKA")

@pytest.mark.parametrize("word", ["FATHA_FATHA", "WAW_HARAKA", "YEH_HARAKA", "DAMMA", "SUKUN"])
def test_uniformate2_2(word):
    assert uniformate2(word) in (word, "NOT_DEF_HARAKA")

@pytest.mark.parametrize("word", ["FATHA_FATHA", "WAW_HARAKA", "YEH_HARAKA", "DAMMA", "SUKUN"])
def test_uniformate2_3(word):
    assert uniformate2(word) in (word, "NOT_DEF_HARAKA")

@pytest.mark.parametrize("word", ["FATHA_FATHA", "WAW_HARAKA", "YEH_HARAKA", "DAMMA", "SUKUN"])
def test_uniformate2_4(word):
    assert uniformate2(word) in (word, "NOT_DEF_HARAKA")

@pytest.mark.parametrize("word", ["FATHA_FATHA", "WAW_HARAKA", "YEH_HARAKA", "DAMMA", "SUKUN"])
def test_uniformate2_5(word):
    assert uniformate2(word) in (word, "NOT_DEF_HARAKA")

@pytest.mark.parametrize("word", ["FATHA_FATHA", "WAW_HARAKA", "YEH_HARAKA", "DAMMA", "SUKUN"])
def test_uniformate2_6(word):
    assert uniformate2(word) in (word, "NOT_DEF_HARAKA")

@pytest.mark.parametrize("word", ["FATHA_FATHA", "WAW_HARAKA", "YEH_HARAKA", "DAMMA", "SUKUN"])
def test_uniformate2_7(word):
    assert uniformate2(word) in (word, "NOT_DEF_HARAKA")

@pytest.mark.parametrize("word", ["FATHA_FATHA", "WAW_HARAKA", "YEH_HARAKA", "DAMMA", "SUKUN"])
def test_uniformate2_8(word):
    assert uniformate2(word) in (word, "NOT_DEF_HARAKA")
