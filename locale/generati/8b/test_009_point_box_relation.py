from funzione import point_box_relation

def test_point_box_relation_1():
    u = (0, 0)
    vbox = (10, 20, 30, 40)
    assert point_box_relation(u, vbox) is None

def test_point_box_relation_2():
    u = (5, 25)
    vbox = (10, 20, 30, 40)
    assert point_box_relation(u, vbox) == 4

def test_point_box_relation_3():
    u = (15, 35)
    vbox = (10, 20, 30, 40)
    assert point_box_relation(u, vbox) == 7

def test_point_box_relation_4():
    u = (5, 25)
    vbox = (-10, -20, 0, 0)
    assert point_box_relation(u, vbox) == 2

def test_point_box_relation_5():
    u = (15, 35)
    vbox = (10, 20, 30, 40)
    assert point_box_relation(u, vbox) == 7

def test_point_box_relation_6():
    u = (0, 0)
    vbox = (-100, -200, 100, 200)
    assert point_box_relation(u, vbox) is None
