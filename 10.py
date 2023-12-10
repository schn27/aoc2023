from aocd import data
from aocd import submit

moves = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
next_heading = {
    'L': {'-': 'L', 'F': 'D', 'L': 'U'},
    'R': {'-': 'R', 'J': 'U', '7': 'D'},
    'U': {'|': 'U', 'F': 'R', '7': 'L'},
    'D': {'|': 'D', 'J': 'L', 'L': 'R'}
}

lines = data.split('\n')
lines = list(map(list, lines))

def get_start():
    x, y = 0, 0
    for i, line in enumerate(lines):
        if 'S' in line:
            return (line.index('S'), i)

    return None

def adjust_start(x, y):
    def is_left(c):
        return c in next_heading['L'].keys()
    def is_right(c):
        return c in next_heading['R'].keys()
    def is_up(c):
        return c in next_heading['U'].keys()
    def is_down(c):
        return c in next_heading['D'].keys()

    if y < len(lines) - 1 and x < len(lines[0]) - 1 and is_down(lines[y + 1][x]) and is_right(lines[y][x + 1]):
        lines[y][x] = 'F'
    elif y < len(lines) - 1 and x > 0 and is_down(lines[y + 1][x]) and is_left(lines[y][x - 1]):
        lines[y][x] = '7'
    elif y > 0 and x < len(lines[0]) - 1 and is_up(lines[y - 1][x]) and is_right(lines[y][x + 1]):
        lines[y][x] = 'L'
    elif y > 0 and x > 0 and is_up(lines[y - 1][x]) and is_left(lines[y][x - 1]):
        lines[y][x] = 'J'
    elif y > 0 and y < len(lines) - 1 and is_up(lines[y - 1][x]) and is_down(lines[y + 1][x]):
        lines[y][x] = '|'
    else:
        lines[y][x] = '-'

x, y = get_start()
adjust_start(x, y)

heading = None
for h in next_heading.values():
    if lines[y][x] in h.keys():
        heading = h[lines[y][x]]
        break

loop_pos = set()

while not ((x, y) in loop_pos):
    loop_pos.add((x, y))
    x += moves[heading][0]
    y += moves[heading][1]
    heading = next_heading[heading][lines[y][x]]

submit(int(len(loop_pos) / 2), part='a')

inside = 0

for y, line in enumerate(lines):
    hits = 0
    prev = None
    for x, c in enumerate(line):
        if (x, y) in loop_pos:
            if c == '|':
                hits += 1
            elif prev is None:
                prev = c
            elif c != '-':
                if (prev == 'L' and c == '7') or (prev == 'F' and c == 'J'):
                    hits += 1
                prev = None
        elif (hits % 2) == 1:
            inside += 1

submit(inside, part='b')
