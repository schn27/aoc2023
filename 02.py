from aocd import data
from aocd import submit
import re
import math

colors = ('red', 'green', 'blue')

def parse_game(s):
    left, right = s.split(':')
    game = int(re.findall(r'\d+', left)[0])
    sets = []

    for e in right.split(';'):
        cubes = [0] * len(colors)
        tokens = re.findall(r'\d+ \w+', e)

        for t in tokens:
            t = t.split(' ')
            cubes[colors.index(t[1])] = int(t[0])

        sets.append(cubes)

    return (game, sets)

games = list(map(parse_game, data.split('\n')))

def part1(cubes):
    res = 0

    for game_id, sets in games:
        if all(map(lambda s: all(map(lambda p: p[0] <= p[1], zip(s, cubes))), sets)):
            res += game_id

    return res

def part2():
    res = 0

    for game_id, sets in games:
        cubes = [0] * len(colors)
        for s in sets:
            cubes = list(map(lambda p: max(p), zip(cubes, s)))

        res += math.prod(cubes)

    return res

submit(part1((12, 13, 14)), part='a')
submit(part2(), part='b')
