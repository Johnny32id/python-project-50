from gendiff.scripts.gendiff import generate_diff
import os
import pytest


@pytest.mark.parametrize(
    "path1,path2,format,result",
    [('file1.json', 'file2.json', 'stylish', 'stylish_result.txt'),
     ('file1.json', 'file2.json', 'plain', 'plain_result.txt'),
     ('file1.json', 'file2.json', 'json', 'json_result.json'),
     ('file1.yaml', 'file2.yaml', 'stylish', 'stylish_result.txt'),
     ('file1.yaml', 'file2.yaml', 'plain', 'plain_result.txt'),
     ('file1.yaml', 'file2.yaml', 'json', 'json_result.json'),
     ])
def test_gendiff_json(path1, path2, format, result):
    file1 = os.path.abspath(f'tests/fixtures/{path1}')
    file2 = os.path.abspath(f'tests/fixtures/{path2}')
    expected = open(os.path.abspath(f'tests/fixtures/{result}'), 'r').read()
    assert generate_diff(file1, file2, format) == expected
