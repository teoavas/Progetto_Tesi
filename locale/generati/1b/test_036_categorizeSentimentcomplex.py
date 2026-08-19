import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_1():
    assert categorizeSentimentcomplex(0.5, 0) == "pleased"
    assert categorizeSentimentcomplex(-0.3, 0) == "miserable"
    assert categorizeSentimentcomplex(0.8, 0) == "astonished"

import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_2():
    assert categorizeSentimentcomplex(0.7, -0.1) == "alarmed"
    assert categorizeSentimentcomplex(-0.9, 0.3) == "mad"

import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_3():
    assert categorizeSentimentcomplex(1.2, -0.5) == "angry"
    assert categorizeSentimentcomplex(-1.8, 0.9) == "bored"

import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_4():
    assert categorizeSentimentcomplex(2.5, -1.2) == "tired"
    assert categorizeSentimentcomplex(-3.8, 0.9) == "relaxed"

import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_5():
    assert categorizeSentimentcomplex(1.4, -2.3) == "content"
    assert categorizeSentimentcomplex(-2.9, 0.8) == "calm"

import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_6():
    assert categorizeSentimentcomplex(3.1, -2.5) == "astonished"
    assert categorizeSentimentcomplex(-4.8, 0.9) == "alarmed"

import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_7():
    assert categorizeSentimentcomplex(2.6, -3.1) == "mad"
    assert categorizeSentimentcomplex(-4.5, 0.8) == "bored"

import math
from funzione import categorizeSentimentcomplex

def test_categorizeSentimentcomplex_8():
    assert categorizeSentimentcomplex(1.9, -4.2) == "relaxed"
    assert categorizeSentimentcomplex(-5.7, 0.6) == "content"
