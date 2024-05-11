import pathlib
from .parsers import parse
from .difference import difference
from .formatters import building_format


def generate_diff(file_path_1, file_path_2, format='stylish'):
    extension = pathlib.Path(file_path_1).suffix
    file1_data = open(file_path_1)
    file2_data = open(file_path_2)
    file1 = parse(file1_data, extension)
    file2 = parse(file2_data, extension)
    diff = difference(file1, file2)
    result = building_format(format, diff)
    return result
