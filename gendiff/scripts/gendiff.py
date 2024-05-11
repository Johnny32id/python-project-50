#!/usr/bin/env python3
from gendiff.args_parser import args_parse
from gendiff.diff_builder import generate_diff


def main():
    args = args_parse()
    diff = generate_diff(args.first_file,
                         args.second_file,
                         args.format)
    print(diff)


if __name__ == '__main__':
    main()
