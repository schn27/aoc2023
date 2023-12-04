from aocd import data
from aocd import submit
import re
import math

colors = ('red', 'green', 'blue')

def parse_game(s):
    left, right = s.split(':')
    game_id = int(re.findall(r'\d+', left)[0])
    sets = []

    for e in right.split(';'):
        cubes = [0] * len(colors)
        tokens = re.findall(r'\d+ \w+', e)

        for t in tokens:
            t = t.split(' ')
            cubes[colors.index(t[1])] = int(t[0])

        sets.append(cubes)

    return (game_id, sets)

games = list(map(parse_game, data.split('\n')))

def part1(cubes):
    def is_set_valid(s):
        return all(map(lambda p: p[0] <= p[1], zip(s, cubes)))

    valid_games = filter(lambda g: all(map(is_set_valid, g[1])), games)

    return sum(map(lambda g: g[0], valid_games))

def part2():
    return sum(map(lambda g: math.prod(map(max, zip(*g[1]))), games))

submit(part1((12, 13, 14)), part='a')
submit(part2(), part='b')
