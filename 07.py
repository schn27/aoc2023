from aocd import data
from aocd import submit
import re

hands = map(lambda line: line.split(' '), data.split('\n'))

def to_hex(hand):
    def map_table(c):
        table = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A'}
        return table[c] if c in table else c
    hand[0] = ''.join(map(map_table, [*hand[0]]))

    return (hand[0], int(hand[1]))

hands = list(map(to_hex, hands))

def get_type(hand):
    hand = ''.join(sorted([*hand]))

    if len(re.findall(r'(.)\1\1\1\1', hand)) != 0:
        return 6

    if len(re.findall(r'(.)\1\1\1', hand)) != 0:
        return 5

    if len(re.findall(r'(.)\1(.)\2\2|(.)\3\3(.)\4', hand)) != 0:
        return 4

    if len(re.findall(r'(.)\1\1', hand)) != 0:
        return 3

    if len(re.findall(r'(.)\1.?(.)\2', hand)) != 0:
        return 2

    if len(re.findall(r'(.)\1', hand)) != 0:
        return 1

    return 0

def key(hand):
    return get_type(hand[0]) * 0x100000 + int(hand[0], 16)

def key_j(hand):
    t = get_type(hand[0])
    
    if hand[0].find('B') >= 0:
        for c in ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'C', 'D', 'E']:
            t = max(t, get_type(hand[0].replace('B', c)))

    return t * 0x100000 + int(hand[0].replace('B', '1'), 16)

def get_total(hands):
    total = 0

    for i, h in enumerate(hands):
        total += (i + 1) * h[1]

    return total

submit(get_total(sorted(hands, key=key)), part='a')
submit(get_total(sorted(hands, key=key_j)), part='b')
