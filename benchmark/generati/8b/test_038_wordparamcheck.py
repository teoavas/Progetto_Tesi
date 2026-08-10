from funzione import wordparamcheck

def test_wordparamcheck_1():
    assert wordparamcheck(["test"], [["test", "none"]]) == [True, 0, "test", True, 0, ["NULL"]]

def test_wordparamcheck_2():
    assert wordparamcheck(["test", "test2"], [["test", "more"]]) == [True, 0, "test", True, 1, ["test2"]]

def test_wordparamcheck_3():
    assert wordparamcheck(["test"], [["test", "optional"]]) == [True, 0, "test", True, 0, ["NULL"]]

def test_wordparamcheck_4():
    assert wordparamcheck(["test"], [["test", "skip"]]) == [True, 0, "test", True, 0, ["NULL"]]

def test_wordparamcheck_5():
    assert wordparamcheck(["test"], [["test", "invalid"]]) == [False, -1, "INVALID", False, -1, ["NULL"]]

def test_wordparamcheck_6():
    assert wordparamcheck([], [["test", "none"]]) == [False, -1, "NULL", False, -1, ["NULL"]]

def test_wordparamcheck_7():
    assert wordparamcheck(["test", "test2", "test3"], [["test", "more"]]) == [True, 0, "test", True, 2, ["test2", "test3"]]
