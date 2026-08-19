import pytest
import random
import math

from funzione import columnTransCipher

def test_columnTransCipher_1():
    string = "abc"
    key = [random.choice(string) for _ in range(5)]
    result = columnTransCipher(key)
    assert len(result) == len(string)

def test_columnTransCipher_2():
    string = "12345"
    key = [random.choice(string) for _ in range(10)]
    result = columnTransCipher(key)
    assert len(result) == len(string)

def test_columnTransCipher_3():
    string = "67890"
    key = [random.choice(string) for _ in range(15)]
    result = columnTransCipher(key)
    assert len(result) == len(string)

def test_columnTransCipher_4():
    string = "11111"
    key = [random.choice(string) for _ in range(20)]
    result = columnTransCipher(key)
    assert len(result) == len(string)

def test_columnTransCipher_5():
    string = "22222"
    key = [random.choice(string) for _ in range(25)]
    result = columnTransCipher(key)
    assert len(result) == len(string)

def test_columnTransCipher_6():
    string = "33333"
    key = [random.choice(string) for _ in range(30)]
    result = columnTransCipher(key)
    assert len(result) == len(string)

def test_columnTransCipher_7():
    string = "44444"
    key = [random.choice(string) for _ in range(40)]
    result = columnTransCipher(key)
    assert len(result) == len(string)

def test_columnTransCipher_8():
    string = "55555"
    key = [random.choice(string) for _ in range(50)]
    result = columnTransCipher(key)
    assert len(result) == len(string)
