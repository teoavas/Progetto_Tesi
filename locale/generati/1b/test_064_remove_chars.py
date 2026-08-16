import pytest

def test_remove_chars_1():
    assert remove_chars('Hello, world!', ' ', '\t', None) == 'Hello world'

def test_remove_chars_2():
    assert remove_chars('This is a test.', ' ', '\t', ['\n']) == 'This is a t'

def test_remove_chars_3():
    assert remove_chars('Remove all characters except \' and \'.', ' ', '\t', None) == 'Remove all characters except \' and '

def test_remove_chars_4():
    assert remove_chars('Remove all non-ASCII characters.', ' ', '\t', None) == 'Remove all ASCII characters'

def test_remove_chars_5():
    assert remove_chars('Remove all punctuation marks.', ' ', '\t', None) == 'Remove all punctuation marks'

def test_remove_chars_6():
    assert remove_chars('Remove all special characters except !@#$%^&*()'.split(), ' ', '\t', None) == '!@#$%^&*()'

def test_remove_chars_7():
    assert remove_chars('Remove all non-printable characters.', ' ', '\t', None) == 'Remove all printable characters'

def test_remove_chars_8():
    assert remove_chars('Remove all whitespace except tabs and newline.', ' ', '\t', None) == 'Remove all whitespace except tabs and newline'
