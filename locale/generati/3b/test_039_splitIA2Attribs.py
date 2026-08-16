from funzione import splitIA2Attribs

def test_splitIA2Attribs_1():
    assert splitIA2Attribs("key=value") == {"key": "value"}

def test_splitIA2Attribs_2():
    assert splitIA2Attribs("key=value;subkey=subvalue") == {"key": "value", "subkey": "subvalue"}

def test_splitIA2Attribs_3():
    assert splitIA2Attribs("key=value;subkey1=subvalue1;subkey2=subvalue2") == {"key": "value", "subkey1": "subvalue1", "subkey2": "subvalue2"}

def test_splitIA2Attribs_4():
    assert splitIA2Attribs("key=value;subkey1=value1;subkey2=value2") == {"key": "value", "subkey1": "value1", "subkey2": "value2"}

def test_splitIA2Attribs_5():
    assert splitIA2Attribs("key=value;subkey1=value1;subkey2=value2;subkey3=value3") == {"key": "value", "subkey1": "value1", "subkey2": "value2", "subkey3": "value3"}

def test_splitIA2Attribs_6():
    assert splitIA2Attribs("key=value;subkey1=value1;subkey2=value2;subkey3=value3;subkey4=value4") == {"key": "value", "subkey1": "value1", "subkey2": "value2", "subkey3": "value3", "subkey4": "value4"}

def test_splitIA2Attribs_7():
    assert splitIA2Attribs("key=value;subkey1=value1;subkey2=value2;subkey3=value3;subkey4=value4;subkey5=value5") == {"key": "value", "subkey1": "value1", "subkey2": "value2", "subkey3": "value3", "subkey4": "value4", "subkey5": "value5"}

def test_splitIA2Attribs_8():
    assert splitIA2Attribs("key=value;subkey1=value1;subkey2=value2;subkey3=value3;subkey4=value4;subkey5=value5;subkey6=value6") == {"key": "value", "subkey1": "value1", "subkey2": "value2", "subkey3": "value3", "subkey4": "value4", "subkey5": "value5", "subkey6": "value6"}
