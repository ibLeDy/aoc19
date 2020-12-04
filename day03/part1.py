def add_tuples(tuple1, tuple2):
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]

DIRECTIONS = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

def compute(wire1, wire2):
    intersections = []
    grid = set()
    position = (0, 0)

    for move in wire1.split(','):
        direction, steps = move[0], int(move[1:])
        direction_tuple = DIRECTIONS[direction]

        for _ in range(steps):
            position = add_tuples(position, direction_tuple)
            grid.add(position)

    position = (0, 0)
    for move in wire2.split(','):
        direction, steps = move[0], int(move[1:])
        direction_tuple = DIRECTIONS[direction]

        for _ in range(steps):
            position = add_tuples(position, direction_tuple)
            if position in grid:
                intersections.append(sum(abs(p) for p in position))

    return min(intersections)

with open('input.txt', 'r') as f:  # TODO: move to bottom
    wire1, wire2 = f.read().strip().splitlines()

result = compute(wire1, wire2)
print(result)
