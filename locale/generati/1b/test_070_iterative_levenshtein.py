import pytest

def test_iterative_levenshtein_1():
    assert iterative_levenshtein("kitten", "sitting") == (7, 4, 3, 2)

import pytest

def test_iterative_levenshtein_2():
    assert iterative_levenshtein("", "") == (0, 0, 0, 0)

import pytest

def test_iterative_levenshtein_3():
    assert iterative_levenshtein("abc", "def") == (2, 1, 2, 1)

import pytest

def test_iterative_levenshtein_4():
    assert iterative_levenshtein("", "abc") == (0, 3, 2, 1)

import pytest

def test_iterative_levenshtein_5():
    assert iterative_levenshtein("abc", "") == (0, 4, 3, 2)

import pytest

def test_iterative_levenshtein_6():
    assert iterative_levenshtein("", "abc") == (0, 1, 2, 3)

import pytest

def test_iterative_levenshtein_7():
    assert iterative_levenshtein("abc", "abc") == (0, 0, 0, 0)

import pytest

def test_iterative_levenshtein_8():
    assert iterative_levenshtein("", "") == (0, 0, 0, 0)
