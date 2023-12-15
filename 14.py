from aocd import data
from aocd import submit
import copy

lines = list(map(lambda line: list(line), data.split('\n')))
height = len(lines)
width = len(lines[0])

def move(lines, direction, preserve=False):
    if preserve:
        lines = copy.deepcopy(lines)

    dx, dy = direction

    start = (dx * width + dy * height - 1) if dx + dy > 0 else 1
    end = -1 if dx + dy > 0 else -(dx * width + dy * height)
    ns = dx == 0

    def is_empty(x, y):
        return x >= 0 and x < width and y >= 0 and y < height and lines[y][x] == '.'

    for i in range(start, end, -(dx + dy)):
        for j in range(0, width if ns else height):
            x, y = (j, i) if ns else (i, j)
            if lines[y][x] == 'O':
                lines[y][x] = '.'
                while is_empty(x + dx, y + dy):
                    x += dx
                    y += dy
                lines[y][x] = 'O'

    return lines

def get_load(lines):
    return sum(map(lambda line: (height - line[0]) * sum(map(lambda e: int(e == 'O'), line[1])),
        enumerate(lines)))

def get_pattern(a):
    min_period = 5

    if len(a) > min_period * 2:
        for period in range(min_period, len(a) // 2):
            diff = list(map(lambda e: e[0] - e[1], zip(a[period:], a[:-period])))
            if all(map(lambda e: e == 0, diff[-period:])):
                return period + len(list(filter(lambda e: e != 0, diff))), period

    return None, None

directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

submit(get_load(move(lines, directions[0], preserve=True)), part='a')

scores = []
start, period = None, None

while period is None:
    for d in directions:
        move(lines, d)

    scores.append(get_load(lines))
    start, period = get_pattern(scores)

submit(scores[start + (1000000000 - start - 1) % period], part='b')
