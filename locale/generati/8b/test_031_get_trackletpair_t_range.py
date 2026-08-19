from funzione import get_trackletpair_t_range

def test_get_trackletpair_t_range_1():
    t_min_1, t_max_1, t_min_2, t_max_2 = 0, 10, 5, 15
    window_len = 12
    result = get_trackletpair_t_range(t_min_1, t_max_1, t_min_2, t_max_2, window_len)
    assert result == (t_min_1, t_max_1, t_min_2, t_max_2)

def test_get_trackletpair_t_range_2():
    t_min_1, t_max_1, t_min_2, t_max_2 = 0, 10, 5, 15
    window_len = 11
    result = get_trackletpair_t_range(t_min_1, t_max_1, t_min_2, t_max_2, window_len)
    assert result == (t_max_2-window_len+1, t_max_1, t_min_2, t_max_2)

def test_get_trackletpair_t_range_3():
    t_min_1, t_max_1, t_min_2, t_max_2 = 0, 10, 5, 15
    window_len = 13
    result = get_trackletpair_t_range(t_min_1, t_max_1, t_min_2, t_max_2, window_len)
    assert result == (t_min_1, t_max_1, t_min_2, t_min_1+window_len-1)

def test_get_trackletpair_t_range_4():
    t_min_1, t_max_1, t_min_2, t_max_2 = 0, 10, 5, 15
    window_len = 14
    result = get_trackletpair_t_range(t_min_1, t_max_1, t_min_2, t_max_2, window_len)
    assert result == (t_start_1, t_max_1, t_min_2, t_start_1+window_len-1)

def test_get_trackletpair_t_range_5():
    t_min_1, t_max_1, t_min_2, t_max_2 = 0, 10, 15, 20
    window_len = 12
    result = get_trackletpair_t_range(t_min_1, t_max_1, t_min_2, t_max_2, window_len)
    assert result == (t_min_1, t_max_1, t_min_2, t_max_2)

def test_get_trackletpair_t_range_6():
    t_min_1, t_max_1, t_min_2, t_max_2 = 0, 10, 5, 15
    window_len = 12
    result = get_trackletpair_t_range(t_min_1, t_max_1, t_min_2, t_max_2, window_len)
    assert result == (t_min_1, t_max_1, t_min_2, t_max_2)

def test_get_trackletpair_t_range_7():
    t_min_1, t_max_1, t_min_2, t_max_2 = 0, 10, 5, 15
    window_len = 12
    result = get_trackletpair_t_range(t_min_1, t_max_1, t_min_2, t_max_2, window_len)
    assert result == (t_min_1, t_max_1, t_min_2, t_max_2)

def test_get_trackletpair_t_range_8():
    t_min_1, t_max_1, t_min_2, t_max_2 = 0, 10, 5, 15
    window_len = 12
    result = get_trackletpair_t_range(t_min_1, t_max_1, t_min_2, t_max_2, window_len)
    assert result == (t_min_1, t_max_1, t_min_2, t_max_2)
