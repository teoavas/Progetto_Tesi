from funzione import get_processor_types_from_config_class

def test_get_processor_types_from_config_class_1():
    assert get_processor_types_from_config_class("BertConfig") == ("BertProcessor",)

def test_get_processor_types_from_config_class_2():
    assert get_processor_types_from_config_class("GPTConfig") == ("GPTTokenizer", "GPTFeatureExtractor")

def test_get_processor_types_from_config_class_3():
    assert get_processor_types_from_config_class("RobertaConfig") == ("RobertaImageProcessor",)

def test_get_processor_types_from_config_class_4():
    assert get_processor_types_from_config_class("XLNetConfig") == ("XLNetTokenizer", "XLNetFeatureExtractor")

def test_get_processor_types_from_config_class_5():
    assert get_processor_types_from_config_class("DistilBertConfig") == ("DistilBertProcessor",)

def test_get_processor_types_from_config_class_6():
    assert get_processor_types_from_config_class("DecisionTransformer") == ()

def test_get_processor_types_from_config_class_7():
    assert get_processor_types_from_config_class("EncoderDecoderModel") == ()
