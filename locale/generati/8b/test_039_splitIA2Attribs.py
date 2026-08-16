from funzione import splitIA2Attribs

def test_splitIA2Attribs_1():
    attribsString = "key1=value1;key2=value2"
    expected_result = {"key1": "value1", "key2": "value2"}
    assert splitIA2Attribs(attribsString) == expected_result

def test_splitIA2Attribs_2():
    attribsString = "key1=value1,key2=value2;key3=value3"
    expected_result = {"key1": "value1", "key2": "value2", "key3": "value3"}
    assert splitIA2Attribs(attribsString) == expected_result

def test_splitIA2Attribs_3():
    attribsString = "key1=value1;key2=value2,key3=value3"
    expected_result = {"key1": "value1", "key2": "value2", "key3": "value3"}
    assert splitIA2Attribs(attribsString) == expected_result

def test_splitIA2Attribs_4():
    attribsString = "key1=value1;key2=value2,key3=value3;key4=value4"
    expected_result = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
    assert splitIA2Attribs(attribsString) == expected_result

def test_splitIA2Attribs_5():
    attribsString = "key1=value1,key2=value2;key3=value3"
    expected_result = {"key1": "value1", "key2": "value2", "key3": "value3"}
    assert splitIA2Attribs(attribsString) == expected_result

def test_splitIA2Attribs_6():
    attribsString = "key1=value1;key2=value2,key3=value3,key4=value4"
    expected_result = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
    assert splitIA2Attribs(attribsString) == expected_result

def test_splitIA2Attribs_7():
    attribsString = ""
    expected_result = {}
    assert splitIA2Attribs(attribsString) == expected_result
