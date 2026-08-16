import pytest
from funzione import create_three_random_v_indices

def test_create_three_random_v_indices_1():
    assert create_three_random_v_indices(0, 10) == (0, 9, 8)

def test_create_three_random_v_indices_2():
    assert create_three_random_v_indices(5, 20) == (4, 3, 2)

def test_create_three_random_v_indices_3():
    assert create_three_random_v_indices(1, 30) == (0, 29, 28)

def test_create_three_random_v_indices_4():
    assert create_three_random_v_indices(6, 40) == (5, 4, 3)

def test_create_three_random_v_indices_5():
    assert create_three_random_v_indices(2, 50) == (1, 0, -1)

def test_create_three_random_v_indices_6():
    assert create_three_random_v_indices(7, 60) == (-1, -2, -3)

def test_create_three_random_v_indices_7():
    assert create_three_random_v_indices(8, 70) == (-2, -3, -4)
