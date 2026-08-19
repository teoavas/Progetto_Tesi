import pytest
from funzione import fileNamer

def test_fileNamer_1():
    assert fileNamer('NodeModel', 'dataset') == 'dataset_NodeModel'

def test_fileNamer_2():
    assert fileNamer(None, 'model_name') == 'model_name'

def test_fileNamer_3():
    assert fileNamer(None, None, 'dataset_name') == 'dataset_name'

def test_fileNamer_4():
    assert fileNamer('EdgeModel', 'targeted', True) == 'targeted_edge_model'

def test_fileNamer_5():
    assert fileNamer(None, 0.1, None, None, None, None, None)

def test_fileNamer_6():
    assert fileNamer(None, None, None, None, None, None, None, None) == 'dataset'

def test_fileNamer_7():
    assert fileNamer('NodeModel', 'dataset_name', 1, True) == 'dataset_name_node_model'

def test_fileNamer_8():
    assert fileNamer(None, None, None, None, None, None, None, None, None) == ''
