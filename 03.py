from aocd import data
from aocd import submit
import re

def parse(lines):
    symbols = []
    numbers = []

    for y, line in enumerate(lines):
        for match in re.finditer(r'\d+|[^\d\.]', line):
            if match.group().isdigit():
                numbers.append((int(match.group()), (y, match.start(), match.end())))
            else:
                symbols.append((match.group(), (y, match.start())))

    return (symbols, numbers)

def is_adjacent(symbol, number):
    y, x = symbol[1]
    x_min = number[1][1] - 1
    x_max = number[1][2]
    y_min = number[1][0] - 1
    y_max = number[1][0] + 1
    return y >= y_min and y <= y_max and x >= x_min and x <= x_max

def get_part_numbers(symbols, numbers):
    part_numbers = []

    for n in numbers:
        if any(map(lambda s: is_adjacent(s, n), symbols)):
            part_numbers.append(n[0])

    return part_numbers

def get_gears(symbols, numbers):
    gears = []

    stars = filter(lambda e: e[0] == '*', symbols)

    for s in stars:
        adjacent = list(filter(lambda n: is_adjacent(s, n), numbers))
        if (len(adjacent) == 2):
            gears.append(adjacent[0][0] * adjacent[1][0])

    return gears

symbols, numbers = parse(data.split('\n'))

submit(sum(get_part_numbers(symbols, numbers)), part='a')
submit(sum(get_gears(symbols, numbers)), part='b')
