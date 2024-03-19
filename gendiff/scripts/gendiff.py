#!/usr/bin/env python3
import argparse
import json


def parse():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("-f", "--format", type=str,
                        help="set format of outputs")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return {'first_file': args.first_file, 'second_file': args.second_file}


def generate_diff(file_path_1, file_path_2):
    file_1 = json.load(open(file_path_1))
    file_2 = json.load(open(file_path_2))
    unique_keys = sorted(set(file_1) | set(file_2))
    result = []
    for key in unique_keys:
        if key in file_1 and key not in file_2:
            result.append(f"- {key}: {file_1[key]}")
        if key not in file_1 and key in file_2:
            result.append(f"+ {key}: {file_2[key]}")
        if key in file_1 and key in file_2:
            if file_1[key] == file_2[key]:
                result.append(f"  {key}: {file_1[key]}")
            else:
                result.append(f"- {key}: {file_1[key]}")
                result.append(f"+ {key}: {file_2[key]}")
    result_to_string = '\n'.join(result)
    return result_to_string


def main():
    args = parse()
    diff = generate_diff(args['first_file'], args['second_file'])
    print(f'''{'{'}
{diff}
{'}'}''')


if __name__ == '__main__':
    main()
