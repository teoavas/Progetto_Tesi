import pytest

def test_min_edit_script_1():
    assert min_edit_script("abc", "abcd") == 0

def test_min_edit_script_2():
    assert min_edit_script("abc", "abz") == 3

def test_min_edit_script_3():
    assert min_edit_script("abc", "acb") == 2

def test_min_edit_script_4():
    assert min_edit_script("abc", "acb") == 1

def test_min_edit_script_5():
    assert min_edit_script("abc", "bac") == 0

def test_min_edit_script_6():
    assert min_edit_script("abc", "bca") == 3

def test_min_edit_script_7():
    assert min_edit_script("abc", "cab") == 2

def test_min_edit_script_8():
    assert min_edit_script("abc", "acb") == 1
