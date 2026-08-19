from funzione import deg2HMS

def test_deg2HMS_1():
    assert deg2HMS(ra=12.5) == '- 00 45 00'

def test_deg2HMS_2():
    assert deg2HMS(dec=-23.4, round=True) == '+ 03 25 24'

def test_deg2HMS_3():
    assert deg2HMS(ra=75.6, dec=-12.8) == ('+ 05 01 36', '- 00 48 00')

def test_deg2HMS_4():
    assert deg2HMS(ra=0, round=False) == ''

def test_deg2HMS_5():
    assert deg2HMS(dec=90, round=True) == '+ 00 00 00'

def test_deg2HMS_6():
    assert deg2HMS(ra=-180, dec=0, round=False) == '- 12 00 00'

def test_deg2HMS_7():
    assert deg2HMS(ra=360, dec=90, round=True) == ('+ 24 00 00', '+ 00 00 00')

def test_deg2HMS_8():
    assert deg2HMS(ra=None, dec=None) == ''
