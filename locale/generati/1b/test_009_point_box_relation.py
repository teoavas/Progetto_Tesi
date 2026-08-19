import pytest

def test_point_box_relation_1():
    assert point_box_relation((0, 0), (10, 20)) == 3

def test_point_box_relation_2():
    assert point_box_relation((5, 5), (15, 25)) == 8

def test_point_box_relation_3():
    assert point_box_relation((1, 1), (9, 19)) == 7

def test_point_box_relation_4():
    assert point_box_relation((0, 0), (20, 30)) == None

def test_point_box_relation_5():
    assert point_box_relation((10, 10), (18, 28)) == 6

def test_point_box_relation_6():
    assert point_box_relation((1, 1), (9, 19)) == 4

def test_point_box_relation_7():
    assert point_box_relation((0, 0), (20, 30)) == 2
