import pytest

def test_get_trackletpair_t_range_1():
    t_min_1, t_max_1, t_min_2, t_max_2 = get_trackletpair_t_range(0.5, 1.0, 0.6, 1.3, 10)
    assert t_min_1 <= t_max_1 <= t_min_2 <= t_max_2

def test_get_trackletpair_t_range_2():
    t_min_1, t_max_1, t_min_2, t_max_2 = get_trackletpair_t_range(0.7, 1.4, 0.8, 1.6, 20)
    assert t_min_1 <= t_max_1 <= t_min_2 <= t_max_2

def test_get_trackletpair_t_range_3():
    t_min_1, t_max_1, t_min_2, t_max_2 = get_trackletpair_t_range(0.9, 1.7, 0.95, 1.65, 30)
    assert t_min_1 <= t_max_1 <= t_min_2 <= t_max_2

def test_get_trackletpair_t_range_4():
    t_min_1, t_max_1, t_min_2, t_max_2 = get_trackletpair_t_range(0.95, 1.65, 0.9, 1.55, 40)
    assert t_min_1 <= t_max_1 <= t_min_2 <= t_max_2

def test_get_trackletpair_t_range_5():
    t_min_1, t_max_1, t_min_2, t_max_2 = get_trackletpair_t_range(0.95, 1.65, 0.9, 1.55, 50)
    assert t_min_1 <= t_max_1 <= t_min_2 <= t_max_2

def test_get_trackletpair_t_range_6():
    t_min_1, t_max_1, t_min_2, t_max_2 = get_trackletpair_t_range(0.95, 1.65, 0.9, 1.55, 60)
    assert t_min_1 <= t_max_1 <= t_min_2 <= t_max_2

def test_get_trackletpair_t_range_7():
    t_min_1, t_max_1, t_min_2, t_max_2 = get_trackletpair_t_range(0.95, 1.65, 0.9, 1.55, 70)
    assert t_min_1 <= t_max_1 <= t_min_2 <= t_max_2

def test_get_trackletpair_t_range_8():
    t_min_1, t_max_1, t_min_2, t_max_2 = get_trackletpair_t_range(0.95, 1.65, 0.9, 1.55, 80)
    assert t_min_1 <= t_max_1 <= t_min_2 <= t_max_2
