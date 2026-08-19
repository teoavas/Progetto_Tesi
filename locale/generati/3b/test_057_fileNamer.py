from funzione import fileNamer

def test_fileNamer_1():
    assert fileNamer('NodeModel', 'dataset1') == 'NodeModel_dataset1'

def test_fileNamer_2():
    assert fileNamer(None, None, 'model2') == ''

def test_fileNamer_3():
    assert fileNamer('NodeModel', 'dataset1', 'model2') == 'NodeModel_dataset1_model2'

def test_fileNamer_4():
    assert fileNamer('NodeModel', 'dataset1', model_name='model2') == 'NodeModel_dataset1_model2'

def test_fileNamer_5():
    assert fileNamer(None, None, 'model2', l_inf=10) == 'Linf10_model2'

def test_fileNamer_6():
    assert fileNamer('NodeModel', 'dataset1', model_name='model2', l_inf=10) == 'NodeModel_dataset1_Linf10_model2'

def test_fileNamer_7():
    assert fileNamer('NodeModel', 'dataset1', model_name='model2', l_inf=10, continuous_epochs=5) == 'NodeModel_dataset1_Linf10_model2_K5'
