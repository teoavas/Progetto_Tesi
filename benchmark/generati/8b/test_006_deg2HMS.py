from funzione import deg2HMS

def test_deg2HMS_1():
    assert deg2HMS(ra=12.5) == '- 0 30 0'

def test_deg2HMS_2():
    assert deg2HMS(ra=12.5, round=True) == '- 0 30 0'

def test_deg2HMS_3():
    assert deg2HMS(dec=-12.5) == '+ 0 30 0'

def test_deg2HMS_4():
    assert deg2HMS(dec=-12.5, round=True) == '+ 0 30 0'

def test_deg2HMS_5():
    assert deg2HMS(ra=12.5, dec=-12.5) == ('- 0 30 0', '+ 0 30 0')

def test_deg2HMS_6():
    assert deg2HMS(ra=12.5, dec=-12.5, round=True) == ('- 0 30 0', '+ 0 30 0')

def test_deg2HMS_7():
    assert deg2HMS(ra=12.5, dec=-12.5, round=False) == ('- 0 30 0', '+ 0 30 0')

def test_deg2HMS_8():
    assert deg2HMS(ra=12.5, dec=-12.5, round=True, round=False) == ('- 0 30 0', '+ 0 30 0')
