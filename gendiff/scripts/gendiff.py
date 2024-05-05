#!/usr/bin/env python3
import argparse
from ..generagate_diff import generate_diff


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


def main():
    args = args_parse()
    diff = generate_diff(args['first_file'],
                         args['second_file'],
                         args['format'])
    print(diff)


if __name__ == '__main__':
    main()
