from aocd import data
from aocd import submit
import re

def parse_record(s):
    s, nums = s.split(' ')
    return (s, list(map(int, re.findall(r'\d+', nums))))

records = list(map(parse_record, data.split('\n')))

memo = {}

def get_arrangements(r):
    s, n = r
    key = s + ','.join(map(str, n))

    if key in memo:
        return memo[key]

    bound = len(s) - (sum(n) + len(n) - 2)
    res = 0

    for i in range(0, bound):
        if re.match(rf'^[\?\.]{{{i}}}[\?#]{{{n[0]}}}', s) is None:
            continue

        if len(n) > 1:
            if s[i + n[0]] == '.' or s[i + n[0]] == '?':
                res += get_arrangements((s[i + n[0] + 1:], n[1:]))
        else:
            space2 = s[i + n[0]:]
            if len(space2) == 0 or re.match(r'^[\?\.]+$', space2) is not None:
                res += 1

    memo[key] = res
    return res

def get_arrangements2(r):
    return get_arrangements(('?'.join([r[0]] * 5), r[1] * 5))

submit(sum(map(get_arrangements, records)), part='a')
submit(sum(map(get_arrangements2, records)), part='b')
