from funzione import columnTransCipher
import math
import random

def test_columnTransCipher_1():
    string = "abcdefghijklmnopqrstuvwxyz"
    key = [2, 4, 6]
    result = columnTransCipher(string, key)
    assert len(result) == len(string)

def test_columnTransCipher_2():
    string = "abcdefghijklmnopqrstuvwxyz"
    key = [2, 4, 6]
    result = columnTransCipher(string, key)
    for i in range(len(key)):
        assert result[i*len(key):(i+1)*len(key)] == "".join([string[j] for j in sorted(range(len(key)), key=lambda k: key[k])])

def test_columnTransCipher_3():
    string = "abcdefghijklmnopqrstuvwxyz"
    key = [2, 4, 6]
    result = columnTransCipher(string, key)
    assert all(c.isalpha() for c in result)

def test_columnTransCipher_4():
    string = "abcdefghijklmnopqrstuvwxyz"
    key = [2, 4, 6]
    result = columnTransCipher(string, key)
    assert len(result) == math.ceil(len(string) / len(key)) * len(key)

def test_columnTransCipher_5():
    string = "abcdefghijklmnopqrstuvwxyz"
    key = [2, 4, 6]
    result = columnTransCipher(string, key)
    for i in range(len(key)):
        assert all(c.islower() or c.isupper() for c in result[i*len(key):(i+1)*len(key)])

def test_columnTransCipher_6():
    string = "abcdefghijklmnopqrstuvwxyz"
    key = [2, 4, 6]
    result = columnTransCipher(string, key)
    assert all(len(x) == math.ceil(len(string) / len(key)) for x in result)

def test_columnTransCipher_7():
    string = "abcdefghijklmnopqrstuvwxyz"
    key = [2, 4, 6]
    result = columnTransCipher(string, key)
    assert all(c in string.upper() or c in string.lower() for c in result)

def test_columnTransCipher_8():
    string = "abcdefghijklmnopqrstuvwxyz"
    key = [2, 4, 6]
    result = columnTransCipher(string, key)
    assert len(result) == len(string)
