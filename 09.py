from aocd import data
from aocd import submit
import re

def extrapolate(v):
    buf = [*v]
    depth = 0

    all_zero = False
    while not all_zero:
        prev = buf[depth]
        all_zero = True

        for i in range(depth + 1, len(buf)):
            diff = buf[i] - prev
            prev = buf[i]
            buf[i] = diff
            all_zero = all_zero and diff == 0

        depth += 1

    buf.append(0)

    past = 0
    for j in range(depth, 0, -1):
        past = buf[j - 1] - past
        for i in range(j, len(buf)):
            buf[i] += buf[i - 1]

    return [past, *buf]

values = list(map(lambda line: list(map(int, re.findall(r'-?\d+', line))), data.split('\n')))
values = list(map(extrapolate, values))

submit(sum(map(lambda v: v[-1], values)), part='a')
submit(sum(map(lambda v: v[0], values)), part='b')
