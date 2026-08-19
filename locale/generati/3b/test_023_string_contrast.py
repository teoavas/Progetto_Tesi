from funzione import string_contrast

def test_string_contrast_1():
    assert string_contrast(['a', 'b', None]) == ('aq', '', ['aq'])

def test_string_contrast_2():
    assert string_contrast(['a', 'b', 'c']) == ('', '', ['ab', 'bc'])

def test_string_contrast_3():
    assert string_contrast(['a', None, 'c']) == ('a', 'c', ['a', 'c'])

def test_string_contrast_4():
    assert string_contrast([None, None]) == ('', '', [None])

def test_string_contrast_5():
    assert string_contrast([]) == ('', '', [])

def test_string_contrast_6():
    assert string_contrast(['a']) == ('a', '', [''])

def test_string_contrast_7():
    with pytest.raises(TypeError):
        string_contrast(123)
