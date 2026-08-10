from funzione import judge_1d100_with_7_ver
import math

def test_judge_1d100_with_7_ver_1():
    assert judge_1d100_with_7_ver(100, 100, "N") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_2():
    assert judge_1d100_with_7_ver(100, 50, "N") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_3():
    assert judge_1d100_with_7_ver(100, 1, "N") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_4():
    assert judge_1d100_with_7_ver(100, 100, "H") == ("ハード", "COLOR_SUCCESS")

def test_judge_1d100_with_7_ver_5():
    assert judge_1d100_with_7_ver(100, 50, "H") == ("失敗", "COLOR_FAILURE")

def test_judge_1d100_with_7_ver_6():
    assert judge_1d100_with_7_ver(100, 1, "H") == ("失敗", "COLOR_FAILURE")

def test_judge_1d100_with_7_ver_7():
    assert judge_1d100_with_7_ver(100, 100, "E") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_8():
    assert judge_1d100_with_7_ver(100, 50, "E") == ("イクストリーム", "COLOR_CRITICAL")

def test_judge_1d100_with_7_ver_9():
    assert judge_1d100_with_7_ver(100, 1, "E") == ("イクストリーム", "COLOR_CRITICAL")

def test_judge_1d100_with_7_ver_10():
    assert judge_1d100_with_7_ver(100, 100, "H") == ("ハード", "COLOR_SUCCESS")

def test_judge_1d100_with_7_ver_11():
    assert judge_1d100_with_7_ver(100, 100, "E") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_12():
    assert judge_1d100_with_7_ver(100, 100, "E") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_13():
    assert judge_1d100_with_7_ver(100, 100, "H") == ("ハード", "COLOR_SUCCESS")

def test_judge_1d100_with_7_ver_14():
    assert judge_1d100_with_7_ver(100, 100, "E") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_15():
    assert judge_1d100_with_7_ver(100, 100, "H") == ("ハード", "COLOR_SUCCESS")

def test_judge_1d100_with_7_ver_16():
    assert judge_1d100_with_7_ver(100, 100, "E") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_17():
    assert judge_1d100_with_7_ver(100, 100, "H") == ("ハード", "COLOR_SUCCESS")

def test_judge_1d100_with_7_ver_18():
    assert judge_1d100_with_7_ver(100, 100, "E") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_19():
    assert judge_1d100_with_7_ver(100, 100, "H") == ("ハード", "COLOR_SUCCESS")

def test_judge_1d100_with_7_ver_20():
    assert judge_1d100_with_7_ver(100, 100, "E") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_21():
    assert judge_1d100_with_7_ver(100, 100, "H") == ("ハード", "COLOR_SUCCESS")

def test_judge_1d100_with_7_ver_22():
    assert judge_1d100_with_7_ver(100, 100, "E") == ("成功", "COLOR_NORMAL_SUCCESS")

def test_judge_1d100_with_7_ver_23():
    assert judge_1d100_with_7_ver(100, 100,
