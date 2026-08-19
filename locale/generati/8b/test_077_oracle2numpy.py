from funzione import oracle2numpy

def test_oracle2numpy_1():
    desc = ['name', 'or_n', 0, 10, 5, 2]
    assert oracle2numpy(desc) == "f8"

def test_oracle2numpy_2():
    desc = ['name', 'or_f', 4, 0, 0, 0]
    assert oracle2numpy(desc) == "f4"

def test_oracle2numpy_3():
    desc = ['name', 'or_s', 10, 0, 0, 0]
    assert oracle2numpy(desc) == "S10"

def test_oracle2numpy_4():
    desc = ['name', 'or_n', 0, 10, None, 0]
    assert oracle2numpy(desc) == "f8"

def test_oracle2numpy_5():
    desc = ['name', 'or_f', 8, 0, 0, 0]
    assert oracle2numpy(desc) == "f8"

def test_oracle2numpy_6():
    desc = ['name', 'or_s', 20, 0, 0, 0]
    assert oracle2numpy(desc) == "S20"

def test_oracle2numpy_7():
    desc = ['name', 'or_n', 0, 10, 5, None]
    assert oracle2numpy(desc) == "f8"
