from funzione import splitIA2Attribs

def test_splitIA2Attribs_1():
    assert splitIA2Attribs('key=value;key2=value2') == {'key': 'value', 'key2': 'value2'}

def test_splitIA2Attribs_2():
    assert splitIA2Attribs('key1=value1,key2=value2;key3=value3') == {'key1': 'value1,key2=value2', 'key3': 'value3'}

def test_splitIA2Attribs_3():
    assert splitIA2Attribs('key1=value1;key2=value2,key3=value3') == {'key1': 'value1', 'key2': 'value2,key3=value3'}

def test_splitIA2Attribs_4():
    assert splitIA2Attribs('key1=value1;key2=value2;key3=value3') == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def test_splitIA2Attribs_5():
    assert splitIA2Attribs('key1=value1;key2=value2,key3=value3;key4=value4') == {'key1': 'value1', 'key2': 'value2,key3=value3', 'key4': 'value4'}

def test_splitIA2Attribs_6():
    assert splitIA2Attribs('key1=value1,key2=value2;key3=value3,key4=value4') == {'key1': 'value1,key2=value2', 'key3': 'value3,key4=value4'}

def test_splitIA2Attribs_7():
    assert splitIA2Attribs('key1=value1;key2=value2;key3=value3,key4=value4') == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3,key4=value4'}

def test_splitIA2Attribs_8():
    assert splitIA2Attribs('key1=value1,key2=value2,key3=value3;key4=value4') == {'key1': 'value1,key2=value2,key3=value3', 'key4': 'value4'}
