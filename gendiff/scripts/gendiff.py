#!/usr/bin/env python3
import argparse
import pathlib
from .parsers import parse
from .difference import difference
from .formatters.formatters import building_format


def args_parse():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("-f", "--format", type=str,
                        default='stylish',
                        help="set format of outputs")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return {'first_file': args.first_file, 'second_file': args.second_file,
            'format': args.format}


def generate_diff(file_path_1, file_path_2, format='stylish'):
    extension = pathlib.Path(file_path_1).suffix
    file1_data = open(file_path_1)
    file2_data = open(file_path_2)
    file1 = parse(file1_data, extension)
    file2 = parse(file2_data, extension)
    diff = difference(file1, file2)
    result = building_format(format, diff)
    return result


def main():
    args = args_parse()
    diff = generate_diff(args['first_file'],
                         args['second_file'],
                         args['format'])
    print(diff)


if __name__ == '__main__':
    main()
