INDENTS = '  '
MINUS = '- '
PLUS = '+ '


def value_to_string(value, depth):
    match value:
        case bool():
            return str(value).lower()
        case None:
            return 'null'
        case dict():
            result = ['{']
            for key, value in value.items():
                result.append(
                    f'{INDENTS * 2 * depth}{key}:'
                    f' {value_to_string(value, depth + 1)}'
                )
            result.append(f'{INDENTS * 2 * (depth - 1)}}}')
            return '\n'.join(result)
        case _:
            return value


def stylish(difference, depth=1):
    result = ['{']
    for item in difference:
        match item['type']:
            case 'tree':
                result.append(
                    f"{INDENTS * 2 * depth}{item['key']}:"
                    f" {stylish(item['children'], depth + 1)}")
            case 'unchanged':
                result.append(
                    f"{INDENTS * 2 * depth}{item['key']}:"
                    f" {value_to_string(item['value'], depth + 1)}")
            case 'deleted':
                result.append(
                    f"{INDENTS * (2 * depth - 1)}{MINUS}{item['key']}:"
                    f" {value_to_string(item['value'], depth + 1)}")
            case 'added':
                result.append(
                    f"{INDENTS * (2 * depth - 1)}{PLUS}{item['key']}:"
                    f" {value_to_string(item['value'], depth + 1)}")
            case 'changed':
                result.append(
                    f"{INDENTS * (2 * depth - 1)}{MINUS}{item['key']}:"
                    f" {value_to_string(item['from'], depth + 1)}")
                result.append(
                    f"{INDENTS * (2 * depth - 1)}{PLUS}{item['key']}:"
                    f" {value_to_string(item['to'], depth + 1)}")
    result.append(f'{INDENTS * 2 * (depth - 1)}}}')
    return '\n'.join(result)
