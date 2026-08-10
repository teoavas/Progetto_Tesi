from funzione import formatTime

def test_formatTime_1():
    assert formatTime(0) == ["", "0 hours", "0 minutes", "0 seconds"]

def test_formatTime_2():
    assert formatTime(60) == ["", "0 hours", "1 minute", "0 seconds"]

def test_formatTime_3():
    assert formatTime(3600) == ["", "0 hours", "0 minutes", "0 seconds"]

def test_formatTime_4():
    assert formatTime(86400) == ["1 day", "0 hours", "0 minutes", "0 seconds"]

def test_formatTime_5():
    assert formatTime(86401) == ["1 day", "1 hour", "1 minute", "1 second"]

def test_formatTime_6():
    assert formatTime(-1) == "ERROR: Negative timeDiff"

def test_formatTime_7():
    assert formatTime(1) == ["", "0 hours", "0 minutes", "1 second"]

def test_formatTime_8():
    assert formatTime(3661) == ["1 day", "0 hours", "1 minute", "1 second"]
