from gendiff.scripts.gendiff import generate_diff
import os
stylish_result = open(
    os.path.abspath('tests/fixtures/stylish_result.txt'), 'r').read()
plain_result = open(
    os.path.abspath('tests/fixtures/plain_result.txt'), 'r').read()
json_result = open(
    os.path.abspath('tests/fixtures/json_result.json'), 'r').read()


def test_gendiff_stylish():
    json_file_1 = os.path.abspath('tests/fixtures/file1.json')
    json_file_2 = os.path.abspath('tests/fixtures/file2.json')
    yaml_file_1 = os.path.abspath('tests/fixtures/file1.yaml')
    yaml_file_2 = os.path.abspath('tests/fixtures/file2.yaml')
    assert generate_diff(json_file_1, json_file_2, 'stylish') == stylish_result
    assert generate_diff(yaml_file_1, yaml_file_2, 'stylish') == stylish_result


def test_gendiff_plain():
    json_file_1 = os.path.abspath('tests/fixtures/file1.json')
    json_file_2 = os.path.abspath('tests/fixtures/file2.json')
    yaml_file_1 = os.path.abspath('tests/fixtures/file1.yaml')
    yaml_file_2 = os.path.abspath('tests/fixtures/file2.yaml')
    assert generate_diff(json_file_1, json_file_2, 'plain') == plain_result
    assert generate_diff(yaml_file_1, yaml_file_2, 'plain') == plain_result


def test_gendiff_json():
    json_file_1 = os.path.abspath('tests/fixtures/file1.json')
    json_file_2 = os.path.abspath('tests/fixtures/file2.json')
    yaml_file_1 = os.path.abspath('tests/fixtures/file1.yaml')
    yaml_file_2 = os.path.abspath('tests/fixtures/file2.yaml')
    assert generate_diff(json_file_1, json_file_2, 'json') == json_result
    assert generate_diff(yaml_file_1, yaml_file_2, 'json') == json_result
