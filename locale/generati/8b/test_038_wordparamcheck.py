from funzione import wordparamcheck

def test_wordparamcheck_1():
    givenparams = ["hello", "world"]
    expectedparams = [["hello", "more"], ["foo", "none"]]
    assert wordparamcheck(givenparams, expectedparams) == [True, 0, 'hello', True, -2, ['world']]

def test_wordparamcheck_2():
    givenparams = ["hello", "world"]
    expectedparams = [["foo", "more"], ["bar", "none"]]
    assert wordparamcheck(givenparams, expectedparams) == [False, -1, 'NULL', False, -2, ['NULL']]

def test_wordparamcheck_3():
    givenparams = ["hello", "world"]
    expectedparams = [["foo", "optional"], ["bar", "none"]]
    assert wordparamcheck(givenparams, expectedparams) == [True, 0, 'hello', True, -2, ['world']]

def test_wordparamcheck_4():
    givenparams = []
    expectedparams = [["foo", "more"], ["bar", "none"]]
    assert wordparamcheck(givenparams, expectedparams) == [False, -1, 'NULL', False, 0, ['NULL']]

def test_wordparamcheck_5():
    givenparams = ["hello"]
    expectedparams = [["foo", "more"], ["bar", "none"]]
    assert wordparamcheck(givenparams, expectedparams) == [True, 0, 'hello', True, -1, ['NULL']]

def test_wordparamcheck_6():
    givenparams = ["hello", "world"]
    expectedparams = [["foo", "skip"], ["bar", "none"]]
    assert wordparamcheck(givenparams, expectedparams) == [True, 0, 'hello', True, -2, ['NULL']]

def test_wordparamcheck_7():
    givenparams = ["hello", "world"]
    expectedparams = [["foo", "invalid"], ["bar", "none"]]
    assert wordparamcheck(givenparams, expectedparams) == [False, -1, 'INVALID', False, -2, ['NULL']]
