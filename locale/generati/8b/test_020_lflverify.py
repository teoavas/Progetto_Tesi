from funzione import lflverify
import logging

def test_lflverify_1():
    logging.basicConfig(level=logging.ERROR)
    assert lflverify([1, 2, 'a', [3, 'b']], 'test') == 0

def test_lflverify_2():
    logging.basicConfig(level=logging.ERROR)
    assert lflverify(123, 'test') == 0

def test_lflverify_3():
    logging.basicConfig(level=logging.ERROR)
    assert lflverify([1, [2], 'a'], 'test') == 1

def test_lflverify_4():
    logging.basicConfig(level=logging.ERROR)
    assert lflverify([[1, 'a'], [2, 'b']], 'test') == 3

def test_lflverify_5():
    logging.basicConfig(level=logging.ERROR)
    try:
        lflverify([1, 2, 'a', [3, 'b']], 'test')
    except Exception as e:
        assert str(e) == "Hour test schema type not as defined"

def test_lflverify_6():
    logging.basicConfig(level=logging.ERROR)
    assert lflverify([], 'test') == 0

def test_lflverify_7():
    logging.basicConfig(level=logging.ERROR)
    try:
        lflverify([1, [2], 'a'], 'test')
    except Exception as e:
        assert str(e) == "Hour test schema type not as defined"
