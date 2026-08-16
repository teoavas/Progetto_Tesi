import pytest
from funzione import deg2HMS

def test_deg2HMS_1():
    assert deg2HMS(ra=0, dec=-90) == '00:00 -90'

def test_deg2HMS_2():
    assert deg2HMS(ra=12, dec=30) == '12:30 0'

def test_deg2HMS_3():
    assert deg2HMS(ra=23.5, dec=45) == '23:45 45'

def test_deg2HMS_4():
    assert deg2HMS(ra=-10, dec=60) == '-10:00 60'

def test_deg2HMS_5():
    assert deg2HMS(ra=0, dec=-90, round=True) == '00:00 -90'

def test_deg2HMS_6():
    assert deg2HMS(ra=12, dec=30, round=False) == '12:30 0'
