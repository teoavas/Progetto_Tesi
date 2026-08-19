import pytest

def test_single_defcom_extract_1():
    assert single_defcom_extract(0, ["def", "class"], True) == ""

def test_single_defcom_extract_2():
    assert single_defcom_extract(0, ["def", "class"], False) == ""

def test_single_defcom_extract_3():
    assert single_defcom_extract(1, ["def", "class"], True) == ""

def test_single_defcom_extract_4():
    assert single_defcom_extract(2, ["def", "class"], False) == ""

def test_single_defcom_extract_5():
    assert single_defcom_extract(3, ["def", "class"], True) == ""

def test_single_defcom_extract_6():
    assert single_defcom_extract(4, ["def", "class"], False) == ""

def test_single_defcom_extract_7():
    assert single_defcom_extract(5, ["def", "class"], True) == ""

def test_single_defcom_extract_8():
    assert single_defcom_extract(6, ["def", "class"], False) == ""
