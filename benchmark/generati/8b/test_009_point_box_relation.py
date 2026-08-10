from funzione import point_box_relation

def test_point_box_relation_1():
    assert point_box_relation((0, 0), (0, 0)) == 0

def test_point_box_relation_2():
    assert point_box_relation((0, 0), (1, 1)) == 0

def test_point_box_relation_3():
    assert point_box_relation((0, 1), (0, 0)) == 1

def test_point_box_relation_4():
    assert point_box_relation((0, 1), (1, 1)) == 1

def test_point_box_relation_5():
    assert point_box_relation((0, 1), (0, 1)) == 2

def test_point_box_relation_6():
    assert point_box_relation((0.5, 0.5), (0, 0)) == 4

def test_point_box_relation_7():
    assert point_box_relation((1, 1), (0, 0)) == 8

def test_point_box_relation_8():
    assert point_box_relation((1, 1), (1, 1)) == 9

def test_point_box_relation_9():
    assert point_box_relation((1, 0), (0, 0)) == 7

def test_point_box_relation_10():
    assert point_box_relation((1, 0), (1, 1)) == 6

def test_point_box_relation_11():
    assert point_box_relation((0, 1), (1, 1)) == 3

def test_point_box_relation_12():
    assert point_box_relation((0, 1), (0, 1)) is None

def test_point_box_relation_13():
    assert point_box_relation((1, 1), (1, 1)) is None
