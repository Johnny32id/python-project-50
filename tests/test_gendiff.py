from gendiff.scripts.gendiff import generate_diff
import os
result = open(os.path.abspath('tests/fixtures/flat_result.txt'), 'r').read()


def test_generate_diff_json():
    path_to_file_1 = os.path.abspath('tests/fixtures/file1.json')
    path_to_file_2 = os.path.abspath('tests/fixtures/file2.json')
    assert generate_diff(path_to_file_1, path_to_file_2) == result


def test_generate_diff_yaml():
    path_to_file1 = os.path.abspath('tests/fixtures/file1.yaml')
    path_to_file2 = os.path.abspath('tests/fixtures/file2.yaml')
    assert generate_diff(path_to_file1, path_to_file2) == result
