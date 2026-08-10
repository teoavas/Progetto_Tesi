from funzione import oracle2numpy

def test_oracle2numpy_1():
    desc = ['name', 'or_n', None, 10, None, None]
    assert oracle2numpy(desc) == "f8"

def test_oracle2numpy_2():
    desc = ['name', 'or_n', None, 10, 0, 0]
    assert oracle2numpy(desc) == "i2"

def test_oracle2numpy_3():
    desc = ['name', 'or_n', None, 10, 0, 5]
    assert oracle2numpy(desc) == "i4"

def test_oracle2numpy_4():
    desc = ['name', 'or_n', None, 10, 0, 10]
    assert oracle2numpy(desc) == "i8"

def test_oracle2numpy_5():
    desc = ['name', 'or_n', None, 10, 5, None]
    assert oracle2numpy(desc) == "f8"

def test_oracle2numpy_6():
    desc = ['name', 'or_n', None, 10, 5, 5]
    assert oracle2numpy(desc) == "f4"

def test_oracle2numpy_7():
    desc = ['name', 'or_n', None, 10, 5, 15]
    assert oracle2numpy(desc) == "f8"

def test_oracle2numpy_8():
    desc = ['name', 'or_n', None, 10, 5, 20]
    assert oracle2numpy(desc) == "f16"

def test_oracle2numpy_9():
    desc = ['name', 'or_f', 4, None, None, None]
    assert oracle2numpy(desc) == "f4"

def test_oracle2numpy_10():
    desc = ['name', 'or_f', 8, None, None, None]
    assert oracle2numpy(desc) == "f8"

def test_oracle2numpy_11():
    desc = ['name', 'or_s', 10, None, None, None]
    assert oracle2numpy(desc) == "S10"

def test_oracle2numpy_12():
    desc = ['name', 'or_s', 20, None, None, None]
    assert oracle2numpy(desc) == "S20"

def test_oracle2numpy_13():
    desc = ['name', 'or_s', 10, None, None, None]
    assert oracle2numpy(desc) == "S10"

def test_oracle2numpy_14():
    desc = ['name', 'or_s', 20, None, None, None]
    assert oracle2numpy(desc) == "S20"

def test_oracle2numpy_15():
    desc = ['name', 'or_s', 10, None, None, None]
    assert oracle2numpy(desc) == "S10"

def test_oracle2numpy_16():
    desc = ['name', 'or_s', 20, None, None, None]
    assert oracle2numpy(desc) == "S20"

def test_oracle2numpy_17():
    desc = ['name', 'or_s', 10, None, None, None]
    assert oracle2numpy(desc) == "S10"

def test_oracle2numpy_18():
    desc = ['name', 'or_s', 20, None, None, None]
    assert oracle2numpy(desc) == "S20"

def test_oracle2numpy_19():
    desc = ['name', 'or_s', 10, None, None, None]
    assert oracle2numpy(desc) == "S10"

def test_oracle2numpy_20():
    desc = ['name', 'or_s', 20, None, None, None]
    assert oracle2numpy(desc) == "S20"

def test_oracle2numpy_21():
    desc = ['name', 'or_s', 10, None, None, None]
    assert oracle2numpy(desc) == "S10"

def test_oracle2numpy_22():
    desc = ['name', 'or_s', 20, None, None, None]
    assert oracle2numpy(desc) == "S20"

def test_oracle2numpy_23():
    desc = ['name', 'or_s', 10, None, None, None]
    assert oracle2numpy(desc) == "S10"

def test_oracle2numpy_24():
    desc = ['name', 'or_s', 20, None, None, None]
    assert oracle2numpy(desc) == "S20"

def test_oracle2numpy_25():
    desc = ['name', 'or_s', 10, None, None, None]
    assert oracle2numpy(desc) == "S10"
