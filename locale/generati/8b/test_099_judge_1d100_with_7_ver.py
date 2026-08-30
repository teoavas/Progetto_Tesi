from funzione import judge_1d100_with_7_ver

def test_judge_1d100_with_7_ver_1():
    assert judge_1d100_with_7_ver(100, 101, "H") == ("ファンブル", "COLOR_FUMBLE")

def test_judge_1d100_with_7_ver_2():
    assert judge_1d100_with_7_ver(100, 50, "H") == ("失敗", "COLOR_FAILURE")

def test_judge_1d100_with_7_ver_3():
    assert judge_1d100_with_7_ver(100, 96, "H") == ("ファンブル", "COLOR_FUMBLE")

def test_judge_1d100_with_7_ver_4():
    assert judge_1d100_with_7_ver(100, 50, "E") == ("失敗", "COLOR_FAILURE")

def test_judge_1d100_with_7_ver_5():
    assert judge_1d100_with_7_ver(100, 20, "E") == ("イクストリーム", "COLOR_CRITICAL")

def test_judge_1d100_with_7_ver_6():
    assert judge_1d100_with_7_ver(100, 50, "H") == ("ハード", "COLOR_SUCCESS")

def test_judge_1d100_with_7_ver_7():
    assert judge_1d100_with_7_ver(100, 100, "H") == ("成功", "COLOR_NORMAL_SUCCESS")
