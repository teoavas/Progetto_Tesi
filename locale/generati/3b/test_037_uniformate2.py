from funzione import uniformate2

def test_uniformate2_1():
    assert uniformate2("FATHA") == ('', '')

def test_uniformate2_2():
    assert uniformate2("DAMMA") == ('', '')

def test_uniformate2_3():
    assert uniformate2("KASRA") == ('', '')

def test_uniformate2_4():
    assert uniformate2("FATHA ALEF") == ('YEH', 'ALEF_HARAKA')

def test_uniformate2_5():
    assert uniformate2("DAMMA WAW") == ('WAW', 'WAW_HARAKA')

def test_uniformate2_6():
    assert uniformate2("KASRA YEH") == ('YEH', 'YEH_HARAKA')

def test_uniformate2_7():
    assert uniformate2("FATHA ALEF FATHA") == ('WAW', 'FATHA_FATHA')
