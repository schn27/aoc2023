from aocd import data
from aocd import submit
import re
import math

def get_nums(line):
    return list(map(int, re.findall(r'\d+', line)))

time, distance = list(map(get_nums, data.split('\n')))

def solve(pair):
    t, d = pair
    sqD = math.sqrt(t ** 2 - 4 * (d + 1))
    roots = ((t - sqD) / 2, (t + sqD) / 2)
    return math.floor(roots[1]) - math.ceil(roots[0]) + 1

submit(math.prod(map(solve, zip(time, distance))), part='a')

def to_big_num(nums):
    return int(''.join(map(str, nums)))

submit(solve((to_big_num(time), to_big_num(distance))), part='b')
