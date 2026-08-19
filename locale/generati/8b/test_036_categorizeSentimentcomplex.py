import pytest
import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_1():
    assert categorizeSentimentcomplex(0, 0) == "pleased"

def test_categorizeSentimentcomplex_2():
    assert categorizeSentimentcomplex(math.sqrt(3), math.sqrt(3)) == "happy"

def test_categorizeSentimentcomplex_3():
    assert categorizeSentimentcomplex(math.sqrt(2), math.sqrt(2)) == "delighted"

def test_categorizeSentimentcomplex_4():
    assert categorizeSentimentcomplex(math.sqrt(1.5), math.sqrt(1.5)) == "excited"

def test_categorizeSentimentcomplex_5():
    assert categorizeSentimentcomplex(math.sqrt(2), 0) == "astonished"

def test_categorizeSentimentcomplex_6():
    assert categorizeSentimentcomplex(-math.sqrt(3), math.sqrt(3)) == "alarmed"

def test_categorizeSentimentcomplex_7():
    assert categorizeSentimentcomplex(math.sqrt(2), -math.sqrt(2)) == "mad"
