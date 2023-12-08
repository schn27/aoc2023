from aocd import data
from aocd import submit
from itertools import cycle
import re
import math

instr, _, *net = data.split('\n')

net = map(lambda e: re.findall(r'\w+', e), net)
net = {e[0]: e[1:] for e in net}

def get_steps(start, end):
    steps = 0
    node = start
    it = cycle(instr)

    while re.match(end, node) is None:
        node = net[node][0 if next(it) == 'L' else 1]
        steps += 1

    return steps

submit(get_steps('AAA', 'ZZZ'), part='a')

start_points = filter(lambda k: k[2] == 'A', net.keys())
submit(math.lcm(*map(lambda s: get_steps(s, r'..Z'), start_points)), part='b')
