from funzione import get_processor_types_from_config_class
import collections.abc

def test_get_processor_types_from_config_class_1():
    assert get_processor_types_from_config_class("BertConfig") == ("BertProcessor",)

def test_get_processor_types_from_config_class_2():
    assert get_processor_types_from_config_class("GPTConfig") == ("GPTProcessor", "GPTTokenizer")

def test_get_processor_types_from_config_class_3():
    assert get_processor_types_from_config_class("RobertaConfig") == ("BertProcessor", "RobertaImageProcessor")

def test_get_processor_types_from_config_class_4():
    assert get_processor_types_from_config_class("XLNetConfig") == ("GPTProcessor", "GPTTokenizer", "XLNetFeatureExtractor", "XLNetTokenizer")

def test_get_processor_types_from_config_class_5():
    assert get_processor_types_from_config_class("DistilBertConfig") == ("BertProcessor", "DistilBertTokenizer")

def test_get_processor_types_from_config_class_6():
    assert get_processor_types_from_config_class("InvalidConfig") == ()

def test_get_processor_types_from_config_class_7():
    assert get_processor_types_from_config_class("GPTConfig", allowed_mappings=["tokenizer"]) == ("GPTTokenizer",)

def test_get_processor_types_from_config_class_8():
    assert get_processor_types_from_config_class("BertConfig", allowed_mappings=["processor", "image_processor"]) == ("BertProcessor",)
