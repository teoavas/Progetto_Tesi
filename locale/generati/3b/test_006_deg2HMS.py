from funzione import deg2HMS

def test_deg2HMS_1():
    assert deg2HMS(90) == '0h 0m 0s'

def test_deg2HMS_2():
    assert deg2HMS(-90) == '-0h 0m 0s'

def test_deg2HMS_3():
    assert deg2HMS(45, 30) == ('0h 0m 45s', '0h 30m 0s')

def test_deg2HMS_4():
    assert deg2HMS(-45, -30) == ('-0h 0m 45s', '-0h 30m 0s')

def test_deg2HMS_5():
    assert deg2HMS(90, round=True) == '0h 0m 0s'

def test_deg2HMS_6():
    assert deg2HMS(-90, round=False) == '-0h 0m 0s'

def test_deg2HMS_7():
    assert deg2HMS(None, None) == ''
