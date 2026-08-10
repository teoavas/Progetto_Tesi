from funzione import create_three_random_v_indices
import random
import pytest

def test_create_three_random_v_indices_1():
    current_vector_index = 0
    numOfPop = 10
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert v_index_1 != current_vector_index
    assert v_index_2 != v_index_1
    assert v_index_2 != current_vector_index
    assert v_index_3 != v_index_1
    assert v_index_3 != v_index_2
    assert v_index_3 != current_vector_index

def test_create_three_random_v_indices_2():
    current_vector_index = 5
    numOfPop = 10
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert v_index_1 != current_vector_index
    assert v_index_2 != v_index_1
    assert v_index_2 != current_vector_index
    assert v_index_3 != v_index_1
    assert v_index_3 != v_index_2
    assert v_index_3 != current_vector_index

def test_create_three_random_v_indices_3():
    current_vector_index = 0
    numOfPop = 10
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert 0 <= v_index_1 <= numOfPop
    assert 0 <= v_index_2 <= numOfPop
    assert 0 <= v_index_3 <= numOfPop

def test_create_three_random_v_indices_4():
    current_vector_index = 5
    numOfPop = 10
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert 0 <= v_index_1 <= numOfPop
    assert 0 <= v_index_2 <= numOfPop
    assert 0 <= v_index_3 <= numOfPop

def test_create_three_random_v_indices_5():
    current_vector_index = 0
    numOfPop = 10
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert v_index_1 != v_index_2
    assert v_index_2 != v_index_3
    assert v_index_3 != v_index_1

def test_create_three_random_v_indices_6():
    current_vector_index = 5
    numOfPop = 10
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert v_index_1 != v_index_2
    assert v_index_2 != v_index_3
    assert v_index_3 != v_index_1

def test_create_three_random_v_indices_7():
    current_vector_index = 0
    numOfPop = 10
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert v_index_1 != current_vector_index
    assert v_index_2 != current_vector_index
    assert v_index_3 != current_vector_index

def test_create_three_random_v_indices_8():
    current_vector_index = 5
    numOfPop = 10
    v_index_1, v_index_2, v_index_3 = create_three_random_v_indices(current_vector_index, numOfPop)
    assert v_index_1 != current_vector_index
    assert v_index_2 != current_vector_index
    assert v_index_3 != current_vector_index
