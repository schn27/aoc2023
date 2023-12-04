from aocd import data
from aocd import submit
import re

def get_positions(lines):
    positions = {'numbers': [], 'symbols': []}

    for y, line in enumerate(lines):
        for match in re.finditer(r'\d+|[^\d\.]', line):
            if match.group().isdigit():
                positions['numbers'].append((int(match.group()), (y, match.start(), match.end())))
            else:
                positions['symbols'].append((match.group(), (y, match.start())))

    return positions

def is_adjacent(symbol, number):
    y, x = symbol[1]
    x_min = number[1][1] - 1
    x_max = number[1][2]
    y_min = number[1][0] - 1
    y_max = number[1][0] + 1
    return y >= y_min and y <= y_max and x >= x_min and x <= x_max

def get_part_numbers(positions):
    numbers = []

    for n in positions['numbers']:
        if len(list(filter(lambda s: is_adjacent(s, n), positions['symbols']))) > 0:
            numbers.append(n[0])

    return numbers

def get_gears(positions):
    gears = []

    stars = filter(lambda e: e[0] == '*', positions['symbols'])

    for s in stars:
        adjacent = list(filter(lambda n: is_adjacent(s, n), positions['numbers']))
        if (len(adjacent) == 2):
            gears.append(adjacent[0][0] * adjacent[1][0])

    return gears

positions = get_positions(data.split('\n'))

submit(sum(get_part_numbers(positions)), part='a')
submit(sum(get_gears(positions)), part='b')
