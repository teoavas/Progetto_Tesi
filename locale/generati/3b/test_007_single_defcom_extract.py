from funzione import single_defcom_extract

def test_single_defcom_extract_1():
    assert single_defcom_extract(0, ["def comment body"], False) == "def comment body"

def test_single_defcom_extract_2():
    assert single_defcom_extract(0, ["def comment body", "class comment"], True) == "def comment body"

def test_single_defcom_extract_3():
    assert single_defcom_extract(1, ["def comment body", "class comment"], False) == ""

def test_single_defcom_extract_4():
    assert single_defcom_extract(0, ["\"\"\"comment body\"\"\"", "class comment"], True) == "\"\"\"comment body\"\"\""

def test_single_defcom_extract_5():
    assert single_defcom_extract(1, ["\"\"\"comment body\"\"\"", "class comment"], False) == ""

def test_single_defcom_extract_6():
    assert single_defcom_extract(0, ["'''comment body'''", "class comment"], True) == "'comment body'"

def test_single_defcom_extract_7():
    assert single_defcom_extract(1, ["'''comment body'''", "class comment"], False) == ""
