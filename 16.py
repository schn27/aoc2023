from aocd import data
from aocd import submit

layout = data.split('\n')
width = len(layout[0])
height = len(layout)

def get_energized(beam):
    visited = set()
    energized = set()

    beams = [beam]

    while len(beams) > 0:
        x, y, dx, dy = beams[0]
        beams = beams[1:]

        while (x, y, dx, dy) not in visited and x >= 0 and x < width and y >= 0 and y < height:
            visited.add((x, y, dx, dy))
            energized.add((x, y))

            tile = layout[y][x]

            if tile == '\\' and dx != 0 or tile == '/' and dy != 0:
                dx, dy = (-dy, dx)
            elif tile == '\\' and dy != 0 or tile == '/' and dx != 0:
                dx, dy = dy, -dx
            elif tile == '-' and dy != 0:
                dx, dy = (1, 0)
                beams.append((x - 1, y, -1, 0))
            elif tile == '|' and dx != 0:
                dx, dy = (0, 1)
                beams.append((x, y - 1, 0, -1))

            x += dx
            y += dy

    return len(energized)

submit(get_energized((0, 0, 1, 0)), part='a')

edge = []

for x in range(0, width):
    edge.append((x, 0, 0, 1))
    edge.append((x, height - 1, 0, -1))

for y in range(0, height):
    edge.append((0, y, 1, 0))
    edge.append((width - 1, y, -1, 0))

submit(max(map(get_energized, edge)), part='b')
