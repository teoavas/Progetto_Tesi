from funzione import lflverify
import pytest

def test_lflverify_1():
    assert lflverify([1, 2, 3], "test_json") == 0

def test_lflverify_2():
    with pytest.raises(Exception):
        lflverify("not a list", "test_json")

def test_lflverify_3():
    assert lflverify([[1, 2], [3, 4]], "test_json") == 0

def test_lflverify_4():
    assert lflverify([1, 2, [3, 4]], "test_json") == 0

def test_lflverify_5():
    with pytest.raises(Exception):
        lflverify({"a": 1}, "test_json")

def test_lflverify_6():
    assert lflverify([[1, 2], [3, 4], [5, 6]], "test_json") == 0

def test_lflverify_7():
    with pytest.raises(Exception):
        lflverify([], "test_json")
