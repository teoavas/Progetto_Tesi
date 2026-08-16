import pytest

def test_oracle2numpy_1():
    assert oracle2numpy(("float", 4, "int8")) == "f8"

def test_oracle2numpy_2():
    assert oracle2numpy(("double", 8, "int16")) == "f16"

def test_oracle2numpy_3():
    assert oracle2numpy(("float", 1, "int32")) == "i4"

def test_oracle2numpy_4():
    assert oracle2numpy(("float", 0, None)) == "f8"

def test_oracle2numpy_5():
    assert oracle2numpy(("float", 3, "int64")) == "f16"

def test_oracle2numpy_6():
    assert oracle2numpy(("double", 1, "int8")) == "i8"
