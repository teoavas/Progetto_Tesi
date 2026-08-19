import pytest

def test_string_contrast_1():
    assert string_contrast('hello') == ('he', 'lo', ['h', None, 'e', None])
    assert string_contrast(None) == (None, None, [])

def test_string_contrast_2():
    assert string_contrast(['apple', 'banana']) == ('ap', 'an', ['a', None, 'b', None])

def test_string_contrast_3():
    assert string_contrast(['hello', None]) == (None, None, ['h', None, 'e', None])
    assert string_contrast(None) == (None, None, [])

def test_string_contrast_4():
    assert string_contrast(['apple', 'banana', None]) == ('ap', 'an', ['a', None, 'b', None])

def test_string_contrast_5():
    assert string_contrast(['hello', 'world']) == ('he', 'wo', ['h', None, 'e', None, None, None])
    assert string_contrast(None) == (None, None, [])

def test_string_contrast_6():
    assert string_contrast(['apple', 'banana', 'cherry']) == ('ap', 'an', ['a', None, 'b', None, None])

def test_string_contrast_7():
    with pytest.raises(ValueError):
        string_contrast('hello')
