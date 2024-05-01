#!/usr/bin/env python3

from .stylish import stylish
from .plain import plain
from .json import json_formatter


def building_format(format, difference):
    match format:
        case 'stylish':
            return stylish(difference)
        case 'plain':
            return plain(difference)
        case 'json':
            return json_formatter(difference)
        case _:
            raise TypeError(f'{format} is not available format')
