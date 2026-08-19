from funzione import categorizeSentimentcomplex
import math

def test_categorizeSentimentcomplex_1():
    assert categorizeSentimentcomplex(0, 0) == "pleased"

def test_categorizeSentimentComplex_2():
    assert categorizeSentimentcomplex(-1, -1) == "alarmed"

def test_categorizeSentimentComplex_3():
    assert categorizeSentimentcomplex(math.pi / 4, math.pi / 4) == "happy"

def test_categorizeSentimentComplex_4():
    assert categorizeSentimentcomplex(0.5, -1) == "excited"

def test_categorizeSentimentComplex_5():
    assert categorizeSentimentcomplex(-1, 0) == "mad"

def test_categorizeSentimentComplex_6():
    assert categorizeSentimentcomplex(math.pi / 2, math.pi / 2) == "astonished"

def test_categorizeSentimentComplex_7():
    assert categorizeSentimentcomplex(1, -1) == "angry"
