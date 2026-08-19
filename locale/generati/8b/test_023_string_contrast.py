from funzione import string_contrast

def test_string_contrast_1():
    result = string_contrast(['abc', 'abq', None, 'abcd'])
    expected_prefix, expected_suffix, expected_middle = ('a', '', ['b', 'c', None])
    assert result == (expected_prefix, expected_suffix, expected_middle)

def test_string_contrast_2():
    result = string_contrast(['abc', 'abq', 'abcd'])
    expected_prefix, expected_suffix, expected_middle = ('a', 'd', ['', 'bc'])
    assert result == (expected_prefix, expected_suffix, expected_middle)

def test_string_contrast_3():
    result = string_contrast([None, None, None])
    expected_prefix, expected_suffix, expected_middle = ('', '', [None, None, None])
    assert result == (expected_prefix, expected_suffix, expected_middle)

def test_string_contrast_4():
    result = string_contrast(['abc', 'abq'])
    expected_prefix, expected_suffix, expected_middle = ('a', '', ['b', 'c'])
    assert result == (expected_prefix, expected_suffix, expected_middle)

def test_string_contrast_5():
    result = string_contrast(['abc', None])
    expected_prefix, expected_suffix, expected_middle = ('a', '', ['bc', None])
    assert result == (expected_prefix, expected_suffix, expected_middle)
