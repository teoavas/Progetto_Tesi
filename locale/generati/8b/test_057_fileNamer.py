from funzione import fileNamer

def test_fileNamer_1():
    assert fileNamer(node_model='NodeModel') == 'NodeModel'

def test_fileNamer_2():
    assert fileNamer(dataset_name='DatasetName') == '_DatasetName'

def test_fileNamer_3():
    assert fileNamer(model_name='ModelName', node_model=True) == '_EdgeModel_ModelName'

def test_fileNamer_4():
    assert fileNamer(l_inf=1.0, l_0=None) == '_Linf1'

def test_fileNamer_5():
    assert fileNamer(num_layers=10, seed=None) == '_10Layers'

def test_fileNamer_6():
    assert fileNamer(targeted=False) == 'untargeted'

def test_fileNamer_7():
    assert fileNamer(continuous_epochs=1000, patience=5) == '_1000K_patience5'
