from .utils import rescale_object
from collections.abc import Mapping
from copy import deepcopy
from pathlib import Path
import json


def get_migration(location):
    if isinstance(location, Mapping):
        return location
    elif isinstance(location, str) and Path(location).is_file():
        return json.load(open(location))
    else:
        raise ValueError


def modify_object(obj, dct):
    scale = dct.get("__disaggregation__", 1) * dct.get("__multiplier__", 1)
    if scale != 1:
        obj = rescale_object(obj, scale)
    for k, v in dct.items():
        if k not in ("__disaggregation__", "__multiplier__"):
            obj[k] = v
    return obj


def migrate_data(data, migration):
    migration_data = get_migration(migration)
    lookup = {tuple(x): y for x, y in migration_data["data"]}

    for row in data:
        try:
            new = lookup[tuple([row.get(field) for field in migration_data["fields"]])]
            if isinstance(new, list):
                for dct in new:
                    yield modify_object(deepcopy(row), dct)
            else:
                yield modify_object(row, new)
        except KeyError:
            yield row
