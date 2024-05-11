import json
import yaml


def parse(data, extension):
    match extension:
        case '.json':
            return json.load(data)
        case '.yaml' | '.yml':
            return yaml.load(data, Loader=yaml.Loader)
        case _:
            raise NameError(f"Wrong file extension {extension}")
