from dictlearn.retrieval import Dictionary

from tests.test_util import temporary_content_path, TEST_DICT_JSON

def test_dict():
    with temporary_content_path(TEST_DICT_JSON) as path:
        dict_ = Dictionary(path)
    assert dict_.get_definitions('a') == [['b', 'c'], ['d', 'e']]
    assert dict_.get_definitions('d c') == [['a', 'b']]
