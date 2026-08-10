from funzione import single_defcom_extract

def test_single_defcom_extract_1():
    srcls = [
        "def function1():",
        "    pass",
        "    # This is a comment",
        "    ''' This is a docstring '''",
        "    print('Hello World')"
    ]
    assert single_defcom_extract(0, srcls) == "    ''' This is a docstring '''\n    print('Hello World')"

def test_single_defcom_extract_2():
    srcls = [
        "class MyClass:",
        "    def __init__(self):",
        "        pass",
        "    # This is a comment",
        "    \"\"\" This is a docstring \"\"\""
    ]
    assert single_defcom_extract(0, srcls) == "    \"\"\" This is a docstring \"\"\""

def test_single_defcom_extract_3():
    srcls = [
        "def function1():",
        "    pass",
        "    # This is a comment",
        "    ''' This is a docstring '''",
        "    print('Hello World')"
    ]
    assert single_defcom_extract(1, srcls) == "    # This is a comment\n    ''' This is a docstring '''\n    print('Hello World')"

def test_single_defcom_extract_4():
    srcls = [
        "class MyClass:",
        "    def __init__(self):",
        "        pass",
        "    # This is a comment",
        "    \"\"\" This is a docstring \"\"\""
    ]
    assert single_defcom_extract(1, srcls) == "    def __init__(self):\n        pass\n    # This is a comment\n    \"\"\" This is a docstring \"\"\""

def test_single_defcom_extract_5():
    srcls = [
        "def function1():",
        "    pass",
        "    # This is a comment",
        "    ''' This is a docstring '''",
        "    print('Hello World')"
    ]
    assert single_defcom_extract(2, srcls) == "    # This is a comment\n    ''' This is a docstring '''\n    print('Hello World')"

def test_single_defcom_extract_6():
    srcls = [
        "class MyClass:",
        "    def __init__(self):",
        "        pass",
        "    # This is a comment",
        "    \"\"\" This is a docstring \"\"\""
    ]
    assert single_defcom_extract(2, srcls) == "    def __init__(self):\n        pass\n    # This is a comment\n    \"\"\" This is a docstring \"\"\""

def test_single_defcom_extract_7():
    srcls = [
        "def function1():",
        "    pass",
        "    # This is a comment",
        "    ''' This is a docstring '''",
        "    print('Hello World')"
    ]
    assert single_defcom_extract(3, srcls) == "    ''' This is a docstring '''\n    print('Hello World')"

def test_single_defcom_extract_8():
    srcls = [
        "class MyClass:",
        "    def __init__(self):",
        "        pass",
        "    # This is a comment",
        "    \"\"\" This is a docstring \"\"\""
    ]
    assert single_defcom_extract(3, srcls) == "    \"\"\" This is a docstring \"\"\""
