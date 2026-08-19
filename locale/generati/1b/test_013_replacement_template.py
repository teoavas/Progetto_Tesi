import pytest

def test_replacement_template_1():
    assert replacement_template('123&456', 'A', [0, 2], ['a']) == 'abc'

def test_replacement_template_2():
    assert replacement_template('&123&456', 'B', [0, 3], ['b']) == '&234'

def test_replacement_template_3():
    assert replacement_template('123&456', '`789', [1, 4], ['g']) == '789'

def test_replacement_template_4():
    assert replacement_template('&123&456', '\'789', [0, 5], ['y']) == '&234'

def test_replacement_template_5():
    assert replacement_template('123&456', '$', [1, 3], []) == '567'

def test_replacement_template_6():
    assert replacement_template('&123&456', '.', [0, 4], ['e']) == '&234'

def test_replacement_template_7():
    assert replacement_template('123&456', '?', [2, 5], ['z']) == '&234'

def test_replacement_template_8():
    assert replacement_template('&123&456', '!', [1, 3], []) == '567'
