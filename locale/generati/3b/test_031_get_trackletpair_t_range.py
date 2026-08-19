from funzione import get_trackletpair_t_range

def test_get_trackletpair_t_range_1():
    assert get_trackletpair_t_range(0, 10, 20, 30, 5) == (0, 10, 20, 30)

def test_get_trackletpair_t_range_2():
    assert get_trackletpair_t_range(15, 25, 35, 45, 3) == (15, 25, 35, 45)

def test_get_trackletpair_t_range_3():
    assert get_trackletpair_t_range(10, 20, 30, 40, 2) == (11, 21, 31, 41)

def test_get_trackletpair_t_range_4():
    with pytest.raises(AssertionError):
        get_trackletpair_t_range(15, 25, 35, 45, 1)

def test_get_trackletpair_t_range_5():
    assert get_trackletpair_t_range(10, 20, 30, 40, 3) == (11, 21, 31, 41)

def test_get_trackletpair_t_range_6():
    with pytest.raises(AssertionError):
        get_trackletpair_t_range(15, 25, 35, 45, 0.5)

def test_get_trackletpair_t_range_7():
    assert get_trackletpair_t_range(10, 20, 30, 40, 2) == (11, 21, 31, 41)
