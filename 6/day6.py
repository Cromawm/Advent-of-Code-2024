import numpy as np

def build_matrix() -> list[list[str]]:
    with open("./6/input.txt") as f:
        return [list(line.strip()) for line in f.readlines()]

def find_guard() -> tuple[int,int]: # there will always be a guard so we dont need the extra case
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if matrix[i,j] == '^':
                return (i, j)

def move_guard(matrix) -> int:
    guard_location = find_guard()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    direction = directions[direction_index]

    while in_bounds(guard_location):
        new_location = (guard_location[0] + direction[0], guard_location[1] + direction[1])
        if not in_bounds(new_location):
            matrix[guard_location[0], guard_location[1]] = 'X'
            guard_location = new_location
            return matrix

        if matrix[new_location[0], new_location[1]] == '#':
            direction_index = (direction_index + 1) % 4
            direction = directions[direction_index]
        else:
            matrix[guard_location[0], guard_location[1]] = 'X'
            guard_location = new_location
    
matrix = np.array(build_matrix())
dimensions = matrix.shape

def in_bounds(location: tuple[int, int]) -> bool:
    return 0 <= location[0] < dimensions[0] and 0 <= location[1] < dimensions[1]

print(f"Day six part one: {sum(map(lambda r: sum(map(lambda v: 1 if v == 'X' else 0,r)), move_guard(matrix)))}")