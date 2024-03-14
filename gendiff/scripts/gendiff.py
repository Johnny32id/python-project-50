import argparse
import json
parser = argparse.ArgumentParser(
    description="Compares two configuration files and shows a difference.")
parser.add_argument("-f", "--format", type=str,
                    help="set format of outputs")
parser.add_argument("first_file")
parser.add_argument("second_file")
args = parser.parse_args()


def generate_diff(file_1, file_2):
    unique_keys = set(file_1) | set(file_2)
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
    print(f'''{'{'}
{result_to_string}
{'}'}''')


def main():
    file_1 = json.load(open(args.first_file))
    file_2 = json.load(open(args.second_file))
    generate_diff(file_1, file_2)


if __name__ == '__main__':
    main()
