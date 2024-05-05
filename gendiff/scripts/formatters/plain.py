#!/usr/bin/env python3


def value_to_string(value):
    match value:
        case bool():
            return str(value).lower()
        case None:
            return 'null'
        case dict():
            return '[complex value]'
        case int():
            return value
        case _:
            return f"'{value}'"


def plain(difference, ancentry=''):
    result = []
    for item in difference:
        match item['type']:
            case 'tree':
                result.append(
                    plain(item['children'], f"{ancentry}{item['key']}."))
            case 'unchanged':
                continue
            case 'deleted':
                result.append(
                    f"Property '{ancentry}{item['key']}' was removed")
            case 'added':
                result.append(
                    f"Property '{ancentry}{item['key']}' was added with value: "
                    f"{value_to_string(item['value'])}")
            case 'changed':
                result.append(
                    f"Property '{ancentry}{item['key']}' was updated. "
                    f"From {value_to_string(item['from'])} "
                    f"to {value_to_string(item['to'])}")
    return '\n'.join(result)
