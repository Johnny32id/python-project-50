from gendiff.scripts.gendiff import generate_diff
import os
import pytest
stylish_result = open(
    os.path.abspath('tests/fixtures/stylish_result.txt'), 'r').read()
plain_result = open(
    os.path.abspath('tests/fixtures/plain_result.txt'), 'r').read()
json_result = open(
    os.path.abspath('tests/fixtures/json_result.json'), 'r').read()
json_file_1 = os.path.abspath('tests/fixtures/file1.json')
json_file_2 = os.path.abspath('tests/fixtures/file2.json')
yaml_file_1 = os.path.abspath('tests/fixtures/file1.yaml')
yaml_file_2 = os.path.abspath('tests/fixtures/file2.yaml')


pytestmark = pytest.mark.parametrize("format, expected",
                                     [('stylish', stylish_result),
                                      ('plain', plain_result),
                                      ('json', json_result)])


def test_gendiff_json(format, expected):
    assert generate_diff(json_file_1, json_file_2, format) == expected


def test_gendiff_yaml(format, expected):
    assert generate_diff(yaml_file_1, yaml_file_2, format) == expected
