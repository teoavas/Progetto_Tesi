import pytest

def test_judge_1d100_with_7_ver_1():
    assert judge_1d100_with_7_ver(100, 7, "H") == "ファンブル", "COLOR_FUMBLE"

def test_judge_1d100_with_7_ver_2():
    assert judge_1d100_with_7_ver(100, 7, "E") == "ファンブル", "COLOR_FUMBLE"

def test_judge_1d100_with_7_ver_3():
    assert judge_1d100_with_7_ver(100, 7, "D") == "イクストリーム", "COLOR_CRITICAL"

def test_judge_1d100_with_7_ver_4():
    assert judge_1d100_with_7_ver(100, 7, "C") == "成功", "COLOR_NORMAL_SUCCESS"

def test_judge_1d100_with_7_ver_5():
    assert judge_1d100_with_7_ver(100, 7, "S") == "失敗", "COLOR_FAILURE"

def test_judge_1d100_with_7_ver_6():
    assert judge_1d100_with_7_ver(100, 7, "M") == "ファンブル", "COLOR_FUMBLE"

def test_judge_1d100_with_7_ver_7():
    assert judge_1d100_with_7_ver(100, 7, "L") == "失敗", "COLOR_FAILURE"
