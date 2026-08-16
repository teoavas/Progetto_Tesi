import pytest

def test__remove_strings_1():
    assert _remove_strings("Hello 'world'") == "Hello world"

def test__remove_strings_2():
    assert _remove_strings('"foo"') == '"'

def test__remove_strings_3():
    assert _remove_strings("'bar'") == "'"

def test__remove_strings_4():
    assert _remove_strings('baz') == ''

def test__remove_strings_5():
    assert _remove_strings("qux") == "qux"

def test__remove_strings_6():
    assert _remove_strings('"quux"') == '"'

def test__remove_strings_7():
    assert _remove_strings("'corge'") == "'"

def test__remove_strings_8():
    assert _remove_strings('grault') == 'grault'
