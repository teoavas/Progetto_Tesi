from funzione import create_three_random_v_indices
import random

def test_create_three_random_v_indices_1():
    assert len(create_three_random_v_indices(0, 10)) == 3

def test_create_three_random_v_indices_2():
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(5, 20)
    assert v_index_1 != 5
    assert v_index_2 != 5 and v_index_2 != v_index_1
    assert v_index_3 != 5 and v_index_3 != v_index_1 and v_index_3 != v_index_2

def test_create_three_random_v_indices_3():
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(10, 30)
    assert v_index_1 < v_index_2
    assert v_index_2 < v_index_3

def test_create_three_random_v_indices_4():
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(0, 5)
    assert all(v_index in range(5) for v_index in [v_index_1, v_index_2, v_index_3])

def test_create_three_random_v_indices_5():
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(10, 20)
    assert all(v_index != 10 for v_index in [v_index_1, v_index_2, v_index_3])

def test_create_three_random_v_indices_6():
    with pytest.raises(ValueError):
        create_three_random_v_indices(-1, 5)

def test_create_three_random_v_indices_7():
    with pytest.raises(TypeError):
        create_three_random_v_indices('a', 5)
