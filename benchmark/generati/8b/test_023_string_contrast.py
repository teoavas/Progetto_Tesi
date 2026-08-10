from funzione import string_contrast

def test_string_contrast_1():
    assert string_contrast(['a', 'b', 'c']) == ('', '', ['aq', 'bq', 'cq'])

def test_string_contrast_2():
    assert string_contrast(['a', None, 'c']) == ('', '', ['aq', '', 'cq'])

def test_string_contrast_3():
    assert string_contrast(['a', 'b', None]) == ('', '', ['aq', 'bq', ''])

def test_string_contrast_4():
    assert string_contrast(['a', 'b', 'c', 'd']) == ('', '', ['aq', 'bq', 'cq', 'dq'])

def test_string_contrast_5():
    assert string_contrast(['a', 'b', 'c', 'd', 'e']) == ('', '', ['aq', 'bq', 'cq', 'dq', 'eq'])

def test_string_contrast_6():
    assert string_contrast(['a', 'b', 'c', 'd', 'e', 'f']) == ('', '', ['aq', 'bq', 'cq', 'dq', 'eq', 'fq'])

def test_string_contrast_7():
    assert string_contrast(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ('', '', ['aq', 'bq', 'cq', 'dq', 'eq', 'fq', 'gq'])

def test_string_contrast_8():
    assert string_contrast(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) == ('', '', ['aq', 'bq', 'cq', 'dq', 'eq', 'fq', 'gq', 'hq'])
