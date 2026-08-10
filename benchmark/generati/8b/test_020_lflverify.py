from funzione import lflverify
import logging

def test_lflverify_1():
    logging.basicConfig(level=logging.INFO)
    assert lflverify([1, 2, 3], 'test') == 0

def test_lflverify_2():
    logging.basicConfig(level=logging.INFO)
    assert lflverify([1, 2, 'a'], 'test') == 0

def test_lflverify_3():
    logging.basicConfig(level=logging.INFO)
    assert lflverify([1, [2, 'a']], 'test') == 0

def test_lflverify_4():
    logging.basicConfig(level=logging.INFO)
    assert lflverify([[1, 'a'], [2, 'b']], 'test') == 0

def test_lflverify_5():
    logging.basicConfig(level=logging.INFO)
    assert lflverify([[1, 'a'], [2, 'b'], [3, 'c']], 'test') == 0

def test_lflverify_6():
    logging.basicConfig(level=logging.INFO)
    assert lflverify([[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd']], 'test') == 0

def test_lflverify_7():
    logging.basicConfig(level=logging.INFO)
    assert lflverify([[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd'], [5, 'e']], 'test') == 0

def test_lflverify_8():
    logging.basicConfig(level=logging.INFO)
    assert lflverify([[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd'], [5, 'e'], [6, 'f']], 'test') == 0
