test_formatTime_1 = def test_formatTime_1():
    assert formatTime(0) == ["", "0 hours", "0 minutes", "0 seconds"]

test_formatTime_2 = def test_formatTime_2():
    assert formatTime(3600) == ["", "1 hour", "0 minutes", "0 seconds"]

test_formatTime_3 = def test_formatTime_3():
    assert formatTime(7200) == ["", "2 hours", "0 minutes", "0 seconds"]

test_formatTime_4 = def test_formatTime_4():
    assert formatTime(86400) == ["1 day", "0 hours", "0 minutes", "0 seconds"]

test_formatTime_5 = def test_formatTime_5():
    assert formatTime(-1) == "ERROR: Negative timeDiff"

test_formatTime_6 = def test_formatTime_6():
    assert formatTime(86400 + 3600) == ["2 days", "1 hour", "0 minutes", "0 seconds"]

test_formatTime_7 = def test_formatTime_7():
    assert formatTime(7200 * 10) == ["10 hours", "0 minutes", "0 seconds"]
