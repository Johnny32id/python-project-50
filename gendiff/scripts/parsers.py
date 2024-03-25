import json
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parse(data, extension):
    match extension:
        case '.json':
            return json.load(data)
        case '.yaml' | '.yml':
            return yaml.load(data, Loader=Loader)
