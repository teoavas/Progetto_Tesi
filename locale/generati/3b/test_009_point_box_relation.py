from funzione import point_box_relation

def test_point_box_relation_1():
    assert point_box_relation((0, 0), (10, 20, 30, 40)) == 3

def test_point_box_relation_2():
    assert point_box_relation((5, 5), (10, 20, 30, 40)) == 7

def test_point_box_relation_3():
    assert point_box_relation((0, 0), (10, 20, 30, 40)) in [0, 1, 2, 4, 6, 8]

def test_point_box_relation_4():
    assert point_box_relation((5, 5), (10, 20, 30, 40)) not in [3, 7, 9]

def test_point_box_relation_5():
    assert point_box_relation((0, 0), (0, 0, 0, 0)) == None

def test_point_box_relation_6():
    assert point_box_relation((-1, -1), (10, 20, 30, 40)) in [0, 2, 4]

def test_point_box_relation_7():
    assert point_box_relation((5, 5), (-1, -1, -1, -1)) == None
