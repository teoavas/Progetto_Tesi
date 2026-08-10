import pytest
import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_1():
    assert categorizeSentimentcomplex(1, 0) == "pleased"

def test_categorizeSentimentcomplex_2():
    assert categorizeSentimentcomplex(math.sqrt(2), math.sqrt(2)) == "happy"

def test_categorizeSentimentcomplex_3():
    assert categorizeSentimentcomplex(math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "delighted"

def test_categorizeSentimentcomplex_4():
    assert categorizeSentimentcomplex(math.sqrt(2), math.sqrt(2) * math.sqrt(2) * math.sqrt(2)) == "excited"

def test_categorizeSentimentcomplex_5():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "astonished"

def test_categorizeSentimentcomplex_6():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2) * math.sqrt(2)) == "alarmed"

def test_categorizeSentimentcomplex_7():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "mad"

def test_categorizeSentimentcomplex_8():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "angry"

def test_categorizeSentimentcomplex_9():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "annoyed"

def test_categorizeSentimentcomplex_10():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "miserable"

def test_categorizeSentimentcomplex_11():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "depressed"

def test_categorizeSentimentcomplex_12():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "bored"

def test_categorizeSentimentcomplex_13():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "tired"

def test_categorizeSentimentcomplex_14():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "sleepy"

def test_categorizeSentimentcomplex_15():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2), math.sqrt(2) * math.sqrt(2)) == "relaxed"

def test_categorizeSentimentcomplex_16():
    assert categorizeSentimentcomplex(math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2) * math.sqrt(2
