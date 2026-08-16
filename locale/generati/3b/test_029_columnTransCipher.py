from funzione import columnTransCipher
import math
import random

def test_columnTransCipher_1():
    assert columnTransCipher("Hello, World!") == ...

def test_columnTransCipher_2():
    assert columnTransCipher("abcdefghijklmnopqrstuvwxyz", "123456") == ...

def test_columnTransCipher_3():
    assert columnTransCipher("", "123456") == ""

def test_columnTransCipher_4():
    assert columnTransCipher("Hello, World!", "") == ""

def test_columnTransCipher_5():
    assert columnTransCipher("abcdefghijklmnopqrstuvwxyz", None) == "abcdefghijklmnopqrstuvwxyz"

def test_columnTransCipher_6():
    assert columnTransCipher(None, "123456") == "123456"

def test_columnTransCipher_7():
    assert columnTransCipher("Hello, World!", "1234") == ...

def test_columnTransCipher_8():
    assert columnTransCipher("abcdefghijklmnopqrstuvwxyz", "12345") == ...
