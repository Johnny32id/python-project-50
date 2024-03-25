#!/usr/bin/env python3
import argparse
import pathlib
from .parsers import parse


def args_parse():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("-f", "--format", type=str,
                        help="set format of outputs")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return {'first_file': args.first_file, 'second_file': args.second_file}


def generate_diff(file_path_1, file_path_2):
    extension = pathlib.Path(file_path_1).suffix
    file1_data = open(file_path_1)
    file2_data = open(file_path_2)
    file1 = parse(file1_data, extension)
    file2 = parse(file2_data, extension)
    unique_keys = set(file1) | set(file2)
    sorted_keys = sorted(unique_keys)
    result = []
    for key in sorted_keys:
        if key in file1 and key not in file2:
            result.append(f"- {key}: {file1[key]}")
        if key not in file1 and key in file2:
            result.append(f"+ {key}: {file2[key]}")
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                result.append(f"  {key}: {file1[key]}")
            else:
                result.append(f"- {key}: {file1[key]}")
                result.append(f"+ {key}: {file2[key]}")
    result_to_string = '\n'.join(result)
    return result_to_string


def main():
    args = args_parse()
    diff = generate_diff(args['first_file'], args['second_file'])
    print(f'''{'{'}
{diff}
{'}'}''')


if __name__ == '__main__':
    main()
