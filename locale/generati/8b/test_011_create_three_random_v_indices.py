from funzione import create_three_random_v_indices
import random

def test_create_three_random_v_indices_1():
    numOfPop = 10
    current_vector_index = 5
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert isinstance(v_index_1, int) and isinstance(v_index_2, int) and isinstance(v_index_3, int)

def test_create_three_random_v_indices_2():
    numOfPop = 10
    current_vector_index = 5
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert 0 <= v_index_1 < numOfPop and 0 <= v_index_2 < numOfPop and 0 <= v_index_3 < numOfPop

def test_create_three_random_v_indices_3():
    numOfPop = 10
    current_vector_index = 5
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert v_index_1 != current_vector_index and v_index_2 != current_vector_index and v_index_3 != current_vector_index

def test_create_three_random_v_indices_4():
    numOfPop = 10
    current_vector_index = 5
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert v_index_1 != v_index_2 and v_index_2 != v_index_3 and v_index_3 != v_index_1

def test_create_three_random_v_indices_5():
    numOfPop = 10
    current_vector_index = 0
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert v_index_1 != current_vector_index and v_index_2 != current_vector_index and v_index_3 != current_vector_index

def test_create_three_random_v_indices_6():
    numOfPop = 10
    current_vector_index = 5
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert len(set([v_index_1, v_index_2, v_index_3])) == 3

def test_create_three_random_v_indices_7():
    numOfPop = 10
    current_vector_index = 5
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert isinstance(create_three_random_v_indices(current_vector_index, numOfPop), tuple)

def test_create_three_random_v_indices_8():
    numOfPop = 10
    current_vector_index = 5
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert len(v_index_1) == 1 and len(v_index_2) == 1 and len(v_index_3) == 1
