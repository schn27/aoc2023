from aocd import data
from aocd import submit
import re

steps = ''.join(data.split('\n')).split(',')

def get_hash(s):
    v = 0
    for c in s:
        v = ((v + ord(c)) * 17) % 256
    return v

submit(sum(map(get_hash, steps)), part='a')

boxes = [[] for i in range(0, 256)]

for s in steps:
    label, op, lens = re.findall(r'(\w+)([-=])(\d*)', s)[0]
    box = get_hash(label)

    if op == '=':
        lens = int(lens)
        try:
            index = list(map(lambda e: e[0], boxes[box])).index(label)
            boxes[box][index][1] = lens
        except:
            boxes[box].append([label, lens])
    elif op == '-':
        try:
            index = list(map(lambda e: e[0], boxes[box])).index(label)
            boxes[box] = boxes[box][:index] + boxes[box][index + 1:]
        except:
            pass

power = 0

for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        power += (i + 1) * (j + 1) * lens[1]

submit(power, part='b')
