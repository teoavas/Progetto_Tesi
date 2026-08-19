from funzione import make_similar

def test_make_similar_1():
    assert make_similar([1, 2, 3], [1, 2]) == ...

def test_make_similar_2():
    assert make_similar([4, 5, 6], [4, 6]) == ...

def test_make_similar_3():
    assert make_similar([7, 8, 9], [7, 9]) == ...

def test_make_similar_4():
    assert make_similar([1, 2, 3, 4], [1, 3]) == ...

def test_make_similar_5():
    with pytest.raises(TypeError):
        make_similar('a', [1, 2])

def test_make_similar_6():
    with pytest.raises(TypeError):
        make_similar([1, 2], 'a')

def test_make_similar_7():
    assert make_similar([], []) == 0
