import pytest

def test_lumen_type_1():
    assert lumen_type(['ICM', 0, 'mi'], {'I': 0, 'C': 0}, [], [], [], 'hexagonal') == {'I': 0, 'C': 0, 'mi': 'ICMmi'}

def test_lumen_type_2():
    assert lumen_type(['TE', 1, 'bi'], {'T': 0, 'E': 0, 'i': 0}, [], [], [], 'hexagonal') == {'T': 0, 'E': 0, 'i': 'TEbi'}

def test_lumen_type_3():
    assert lumen_type(['ICM', 2, 'mi'], {'I': 1, 'C': 1, 'm': 1}, [], [], [], 'hexagonal') == {'I': 1, 'C': 1, 'm': 'ICMmi'}

def test_lumen_type_4():
    assert lumen_type(['wild_mutants', 0, 'bi'], {'w': 0, 'i': 0, 'd': 0}, [], [], [], 'hexagonal') == {'w': 0, 'i': 'wild_mutantsbi'}

def test_lumen_type_5():
    assert lumen_type(['mutantsmi', 1, 'mi'], {'m': 1, 'u': 1, 'n': 1}, [], [], [], 'hexagonal') == {'m': 1, 'u': 'mutantsmi', 'n': 'wild_mutantsmi'}

def test_lumen_type_6():
    assert lumen_type(['ICM', 0, 'bi'], {'I': 2, 'C': 2}, ['w', 'i'], [], [], 'hexagonal') == {'I': 2, 'C': 2, 'w': 'ICMiwi'}

def test_lumen_type_7():
    assert lumen_type(['wild_mutants', 0, 'mi'], {'w': 1, 'i': 1}, ['m', 'u'], [], [], 'hexagonal') == {'w': 1, 'i': 'wild_mutantsmi', 'm': 'mutantsmi'}

def test_lumen_type_8():
    assert lumen_type(['ICM', 0, 'bi'], {'I': 3, 'C': 3}, ['T', 'E'], [], [], 'hexagonal') == {'I': 3, 'C': 3, 'T': 'TEbi'}
