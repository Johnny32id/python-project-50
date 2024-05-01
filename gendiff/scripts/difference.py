#!/usr/bin/env python3


def difference(first_data, second_data):
    unique_keys = set(first_data) | set(second_data)
    sorted_keys = sorted(unique_keys)
    result = []
    for key in sorted_keys:
        value_before = first_data.get(key)
        value_after = second_data.get(key)
        if key in first_data and key not in second_data:
            result.append(
                {
                    'key': key, 'type': 'deleted', 'value': value_before
                })
        elif key not in first_data and key in second_data:
            result.append(
                {
                    'key': key, 'type': 'added', 'value': value_after
                })
        elif isinstance(value_before, dict) and isinstance(value_after, dict):
            result.append(
                {
                    'key': key, 'type': 'tree',
                    'children': difference(value_before, value_after)
                })
        elif value_before == value_after:
            result.append(
                {
                    'key': key, 'type': 'unchanged', 'value': value_before
                })
        else:
            result.append({'key': key, 'type': 'changed',
                           'from': value_before, 'to': value_after})
    return result
