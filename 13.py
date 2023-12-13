from aocd import data
from aocd import submit
import re

patterns = list(map(lambda p: p.split('\n'), data.split('\n\n')))

def get_reflections(pattern):
    def get_v(p):
        indexes = []
        for i in range(1, len(p)):
            up = p[max(0, 2 * i - len(p)) : i]
            down = p[i : min(len(p), 2 * i)]

            if all(map(lambda e: e[0] == e[1], zip(up, reversed(down)))):
                indexes.append(i)
        return indexes

    transposed = [''.join(map(lambda e: e[i], pattern)) for i in range(0, len(pattern[0]))]
    return (get_v(pattern), get_v(transposed))

def get_score(pattern):
    v, h = get_reflections(pattern)
    return v[0] * 100 if len(v) > 0 else h[0]

def get_score_smudge(pattern):
    ov, oh = get_reflections(pattern)

    for y, line in enumerate(pattern):
        for x, c in enumerate(line):
            s = list(pattern[y])
            s[x] ='#' if c == '.' else '.'
            pattern[y] = ''.join(s)
            v, h = get_reflections(pattern)
            pattern[y] = line
            v = list(filter(lambda e: e not in ov, v))
            h = list(filter(lambda e: e not in oh, h))
            if len(v) > 0 or len(h) > 0:
                return v[0] * 100 if len(v) > 0 else h[0]

    return ov[0] * 100 if len(ov) > 0 else oh[0]

submit(sum(map(get_score, patterns)), part='a')
submit(sum(map(get_score_smudge, patterns)), part='b')
