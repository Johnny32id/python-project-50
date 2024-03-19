from gendiff.scripts.gendiff import generate_diff
import os


def test_generate_diff_json():
    path_to_file_1 = os.path.abspath('tests/fixtures/file1.json')
    path_to_file_2 = os.path.abspath('tests/fixtures/file2.json')
    result = open(os.path.abspath('tests/fixtures/flat_result.txt'), 'r').read()
    assert generate_diff(path_to_file_1, path_to_file_2) == result
