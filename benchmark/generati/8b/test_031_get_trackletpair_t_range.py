from funzione import get_trackletpair_t_range

def test_get_trackletpair_t_range_1():
    assert get_trackletpair_t_range(1, 5, 6, 10, 3) == (1, 5, 6, 10)

def test_get_trackletpair_t_range_2():
    assert get_trackletpair_t_range(1, 5, 6, 10, 5) == (1, 5, 6, 10)

def test_get_trackletpair_t_range_3():
    assert get_trackletpair_t_range(1, 5, 6, 10, 2) == (1, 5, 6, 10)

def test_get_trackletpair_t_range_4():
    assert get_trackletpair_t_range(1, 5, 6, 10, 1) == (1, 5, 6, 10)

def test_get_trackletpair_t_range_5():
    assert get_trackletpair_t_range(1, 5, 6, 10, 7) == (4, 5, 6, 10)

def test_get_trackletpair_t_range_6():
    assert get_trackletpair_t_range(1, 5, 6, 10, 8) == (4, 5, 6, 10)

def test_get_trackletpair_t_range_7():
    assert get_trackletpair_t_range(1, 5, 6, 10, 9) == (4, 5, 6, 10)

def test_get_trackletpair_t_range_8():
    assert get_trackletpair_t_range(1, 5, 6, 10, 10) == (1, 5, 6, 10)
