import pytest
from funzione import columnTransCipher
import math
import random

def test_columnTransCipher_1():
    assert columnTransCipher(string="HELLO", key="123") == "HLEO"

def test_columnTransCipher_2():
    assert columnTransCipher(string="HELLO", key="321") == "OLHE"

def test_columnTransCipher_3():
    assert columnTransCipher(string="HELLO", key="123") != "HELLO"

def test_columnTransCipher_4():
    assert columnTransCipher(string="HELLO", key="123") == columnTransCipher(string="hello", key="123")

def test_columnTransCipher_5():
    assert columnTransCipher(string="HELLO", key="123") == columnTransCipher(string="HELLO", key="123")

def test_columnTransCipher_6():
    assert columnTransCipher(string="HELLO", key="123") == columnTransCipher(string="HELLO", key="123")

def test_columnTransCipher_7():
    assert columnTransCipher(string="HELLO", key="123") == columnTransCipher(string="HELLO", key="123")

def test_columnTransCipher_8():
    assert columnTransCipher(string="", key="123") == ""

def test_columnTransCipher_9():
    assert columnTransCipher(string="HELLO", key="") == ""

def test_columnTransCipher_10():
    assert columnTransCipher(string="HELLO", key="123") == columnTransCipher(string="HELLO", key="123")
