from funzione import make_similar

def test_make_similar_1():
    nums = [1, 3, 5]
    target = [1, 3, 5]
    assert make_similar(nums, target) == 0

def test_make_similar_2():
    nums = [2, 4, 6]
    target = [2, 4, 6]
    assert make_similar(nums, target) == 0

def test_make_similar_3():
    nums = [1, 3, 5]
    target = [2, 4, 6]
    assert make_similar(nums, target) == 0

def test_make_similar_4():
    nums = [1, 3, 5]
    target = [1, 3, 5, 7]
    assert make_similar(nums, target) == 0

def test_make_similar_5():
    nums = [2, 4, 6]
    target = [2, 4, 6, 8]
    assert make_similar(nums, target) == 0

def test_make_similar_6():
    nums = [1, 3, 5, 7]
    target = [1, 3, 5, 7]
    assert make_similar(nums, target) == 0

def test_make_similar_7():
    nums = [2, 4, 6, 8]
    target = [2, 4, 6, 8]
    assert make_similar(nums, target) == 0

def test_make_similar_8():
    nums = [1, 3, 5, 7]
    target = [2, 4, 6, 8]
    assert make_similar(nums, target) == 0
