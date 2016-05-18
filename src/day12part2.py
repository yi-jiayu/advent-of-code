import re
import json as JSON


def count_digits(json: dict) -> int:
    accum = 0
    for item in json.values():
        if isinstance(item, dict):
            if 'red' in item.values():
                continue
            else:
                accum += count_digits(item)
        elif isinstance(item, list):
            for nested_item in item:
                if isinstance(nested_item, dict):
                    count_digits(nested_item)
                else:
                    if isinstance(nested_item, int):
                        accum += nested_item
        else:
            if isinstance(item, int):
                accum += item

    return accum


def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))


with open('../input/day12.txt') as f:
    json = JSON.load(f)  # type: dict

print(n(json))
accum = 0

print(json)

print(count_digits(json))
