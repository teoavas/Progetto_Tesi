from funzione import wordparamcheck

def test_wordparamcheck_1():
    assert wordparamcheck([1, 2], [3, "more"]) == (True, 0, 2, True, 1, [1, 2])

def test_wordparamcheck_2():
    assert wordparamcheck([1, 2, 3], [4, "none"]) == (False, -1, "NULL", False, 0, ["NULL"])

def test_wordparamcheck_3():
    assert wordparamcheck([1, 2, 3], [5, "optional"]) == (True, 1, 2, True, 2, [1, 3])

def test_wordparamcheck_4():
    assert wordparamcheck([1, 2, 3], [6, "skip"]) == (False, -1, "NULL", False, 0, ["NULL"])

def test_wordparamcheck_5():
    assert wordparamcheck([], []) == (True, -1, "NULL", True, 0, ["NULL"])

def test_wordparamcheck_6():
    assert wordparamcheck([1], [2, "more"]) == (False, -1, "NULL", False, 0, ["NULL"])

def test_wordparamcheck_7():
    assert wordparamcheck([1, 2, 3], [4, "none"]) == (False, -1, "NULL", False, 0, ["NULL"])
