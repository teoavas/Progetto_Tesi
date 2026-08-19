import pytest

def test_count_leading_digits_var2_1():
    assert count_leading_digits_var2(111) == 4
    assert count_leading_digits_var2(222) == 3
    assert count_leading_digits_var2(333) == 2
    assert count_leading_digits_var2(444) == 2

def test_count_leading_digits_var2_2():
    assert count_leading_digits_var2(1001) == 4
    assert count_leading_digits_var2(2002) == 3
    assert count_leading_digits_var2(3003) == 2
    assert count_leading_digits_var2(4004) == 2

def test_count_leading_digits_var2_3():
    assert count_leading_digits_var2(10000) == 8
    assert count_leading_digits_var2(20000) == 7
    assert count_leading_digits_var2(30000) == 6
    assert count_leading_digits_var2(40000) == 5

def test_count_leading_digits_var2_4():
    assert count_leading_digits_var2(100000) == 9
    assert count_leading_digits_var2(200000) == 8
    assert count_leading_digits_var2(300000) == 7
    assert count_leading_digits_var2(400000) == 6

def test_count_leading_digits_var2_5():
    assert count_leading_digits_var2(1000000) == 10
    assert count_leading_digits_var2(2000000) == 9
    assert count_leading_digits_var2(3000000) == 8
    assert count_leading_digits_var2(4000000) == 7

def test_count_leading_digits_var2_6():
    assert count_leading_digits_var2(10000000) == 11
    assert count_leading_digits_var2(20000000) == 10
    assert count_leading_digits_var2(30000000) == 9
    assert count_leading_digits_var2(40000000) == 8

def test_count_leading_digits_var2_7():
    assert count_leading_digits_var2(100000000) == 12
    assert count_leading_digits_var2(200000000) == 11
    assert count_leading_digits_var2(300000000) == 10
    assert count_leading_digits_var2(400000000) == 9

def test_count_leading_digits_var2_8():
    assert count_leading_digits_var2(1000000000) == 13
    assert count_leading_digits_var2(2000000000) == 12
    assert count_leading_digits_var2(3000000000) == 11
    assert count_leading_digits_var2(4000000000) == 10
