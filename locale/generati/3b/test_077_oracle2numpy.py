from funzione import oracle2numpy

def test_oracle2numpy_1():
    assert oracle2numpy(("or_n", 0, None, None, None)) == "f8"

def test_oracle2numpy_2():
    assert oracle2numpy(("or_f", 4, None, None, None)) == "f4"

def test_oracle2numpy_3():
    assert oracle2numpy(("or_s", 1, None, None, None)) == "S1"

def test_oracle2numpy_4():
    assert oracle2numpy(("or_n", 0, 8, None, None)) == "f8"

def test_oracle2numpy_5():
    assert oracle2numpy(("or_f", 8, None, None, None)) == "f8"

def test_oracle2numpy_6():
    assert oracle2numpy(("or_n", 0, None, 4, None)) == "i2"

def test_oracle2numpy_7():
    assert oracle2numpy(("or_n", 0, None, None, 0)) == "f8"
