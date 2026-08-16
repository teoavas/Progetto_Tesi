import pytest

def test_splitIA2Attribs_1():
    attribsString = "key1=value1,subkey1=value1.1;key2=value2"
    expected = {"key1": "value1", "subkey1": "value1.1"}
    assert splitIA2Attribs(attribsString) == expected

def test_splitIA2Attribs_2():
    attribsString = "key1=value1,subkey1=value1.1,key3=value3"
    expected = {"key1": "value1", "subkey1": "value1.1"}
    assert splitIA2Attribs(attribsString) == expected

def test_splitIA2Attribs_3():
    attribsString = "key1=value1,subkey1=value1.1,key4=value4"
    expected = {"key1": "value1", "subkey1": "value1.1"}
    assert splitIA2Attribs(attribsString) == expected

def test_splitIA2Attribs_4():
    attribsString = "key1=value1,subkey1=value1.1,key5=value5"
    expected = {"key1": "value1", "subkey1": "value1.1"}
    assert splitIA2Attribs(attribsString) == expected

def test_splitIA2Attribs_5():
    attribsString = "key1=value1,subkey1=value1.1,key6=value6"
    expected = {"key1": "value1", "subkey1": "value1.1"}
    assert splitIA2Attribs(attribsString) == expected

def test_splitIA2Attribs_6():
    attribsString = "key1=value1,subkey1=value1.1,key7=value7"
    expected = {"key1": "value1", "subkey1": "value1.1"}
    assert splitIA2Attribs(attribsString) == expected

def test_splitIA2Attribs_7():
    attribsString = "key1=value1,subkey1=value1.1,key8=value8"
    expected = {"key1": "value1", "subkey1": "value1.1"}
    assert splitIA2Attribs(attribsString) == expected

def test_splitIA2Attribs_8():
    attribsString = ""
    expected = {}
    assert splitIA2Attribs(attribsString) == expected
