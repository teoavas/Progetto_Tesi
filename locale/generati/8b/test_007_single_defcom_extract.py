from funzione import single_defcom_extract

def test_single_defcom_extract_1():
    srcls = ["import os", "def main():", "    print('Hello World')"]
    assert single_defcom_extract(0, srcls) == ""

def test_single_defcom_extract_2():
    srcls = ["import os", "class MyClass:", "    def __init__(self):", "        pass"]
    assert single_defcom_extract(1, srcls) == ""

def test_single_defcom_extract_3():
    srcls = ["import os", "def main():", "    print('Hello World')", '"""This is a docstring."""']
    assert single_defcom_extract(0, srcls) == '"""This is a docstring."""'

def test_single_defcom_extract_4():
    srcls = ["import os", "class MyClass:", "    def __init__(self):", "        pass", "'''This is another docstring.'''"]
    assert single_defcom_extract(1, srcls) == "'''This is another docstring.'''"

def test_single_defcom_extract_5():
    srcls = ["import os", "class MyClass:", "    def __init__(self):", "        pass", '"""This is a docstring."""']
    assert single_defcom_extract(1, srcls) == ""

def test_single_defcom_extract_6():
    srcls = ["import os", "def main():", "    print('Hello World')"]
    assert single_defcom_extract(0, srcls, True) == ""
