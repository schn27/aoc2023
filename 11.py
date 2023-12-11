from aocd import data
from aocd import submit
import re

lines = data.split('\n')

galaxies = []

for y, row in enumerate(lines):
    for m in re.finditer('#', row):
        galaxies.append((m.start(), y))

seen = (set(), set())

for g in galaxies:
    seen[0].add(g[0])
    seen[1].add(g[1])

expanding = (
    set(range(0, len(lines[0]))).difference(seen[0]),
    set(range(0, len(lines))).difference(seen[1]))

def get_dist(g1, g2, mul=2):
    (x1, x2), (y1, y2) = map(sorted, zip(g1, g2))
    dist = x2 - x1 + y2 - y1
    dist += len(expanding[0].intersection(set(range(x1, x2)))) * (mul - 1)
    dist += len(expanding[1].intersection(set(range(y1, y2)))) * (mul - 1)
    return dist

sum1 = 0
sum2 = 0

for i, gi in enumerate(galaxies[:-1]):
    for gj in galaxies[i + 1:]:
        sum1 += get_dist(gi, gj)
        sum2 += get_dist(gi, gj, 1000000)

submit(sum1, part='a')
submit(sum2, part='b')
