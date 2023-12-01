from aocd import data
from aocd import submit
import re

def get_numbers_1(lines):
    return map(lambda e: int(e[0] + e[-1]), map(lambda s: re.findall(r'\d', s), lines))

def get_numbers_2(lines):
    table = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    def mapper(s):
        return s if table.get(s) is None else table[s]

    def get(s):
        found = re.findall(rf"(?=(\d|{'|'.join(table.keys())}))", s)
        return int(mapper(found[0]) + mapper(found[-1]))

    return map(get, lines)

lines = data.split('\n')
submit(sum(get_numbers_1(lines)), part='a')
submit(sum(get_numbers_2(lines)), part='b')
