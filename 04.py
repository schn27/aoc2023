from aocd import data
from aocd import submit
import re

def parse_card(line):
    def get_nums(s):
        return list(map(int, re.findall(r'\d+', s)))

    return list(map(get_nums, line.split(':')[1].split('|')))

cards = list(map(parse_card, data.split('\n')))

def get_score(matched):
    return 2 ** (matched - 1) if matched > 0 else 0

cards = list(map(lambda c: len(list(filter(lambda r: r in c[0], c[1]))), cards))

submit(sum(map(get_score, cards)), part='a')

copies = [1] * len(cards)

for i, c in enumerate(cards):
    for j in range(i, min(i + c, len(cards) - 1)):
        copies[j + 1] += copies[i]

submit(sum(copies), part='b')
