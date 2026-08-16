from funzione import uniformate2

def test_uniformate2_1():
    assert uniformate2("ALFATHA") == ("AL", "ALEF_HARAKA")

def test_uniformate2_2():
    assert uniformate2("ADAMMA WAW") == ("AD", "DAMMA WAW_HARAKA")

def test_uniformate2_3():
    assert uniformate2("AKASRA YEH") == ("A", "KASRA YEH_HARAKA")

def test_uniformate2_4():
    assert uniformate2("ASHADDA") == ("A", "SUKUN NOT_DEF_HARAKA")

def test_uniformate2_5():
    assert uniformate2("AFATHA ALEF") == ("A", "ALEF_HARAKA")

def test_uniformate2_6():
    assert uniformate2("ADAMMA WAW SUKUN") == ("AD", "DAMMA WAW_HARAKA")

def test_uniformate2_7():
    assert uniformate2("") == ("", "")

def test_uniformate2_8():
    assert uniformate2("ALFATHA FATHA ALEF") == ("AL", "ALEF_HARAKA")
