def build_matrix() -> list[list[str]]:
    with open("6/input.txt") as f:
        return [list(line.strip()) for line in f.readlines()]

def find_guard(mx: list[list[str]], dimensions: tuple[int, int]) -> tuple[int, int]: # there will always be a guard so we dont need the extra case
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if mx[i][j] == '^':
                return (i, j)

def move_guard(mx: list[list[str]], dimensions: tuple[int, int]) -> list[list[str]]:
    guard_location = find_guard(mx, dimensions)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    direction = directions[direction_index]

    while in_bounds(guard_location, dimensions):
        new_location = (guard_location[0] + direction[0], guard_location[1] + direction[1])
        if not in_bounds(new_location, dimensions):
            mx[guard_location[0]][guard_location[1]] = 'X'
            guard_location = new_location
            return mx

        if mx[new_location[0]][new_location[1]] == '#':
            direction_index = (direction_index + 1) % 4
            direction = directions[direction_index]
        else:
            mx[guard_location[0]][guard_location[1]] = 'X'
            guard_location = new_location
    
def in_bounds(location: tuple[int, int], dimensions: tuple[int, int]) -> bool:
    return 0 <= location[0] < dimensions[0] and 0 <= location[1] < dimensions[1]

def find_path(mx: list[list[str]], dimensions: tuple[int, int]) -> set:
    guard_location = find_guard(mx, dimensions)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    direction = directions[direction_index]
    path = set()

    while in_bounds(guard_location, dimensions):
        path.add(guard_location)
        new_location = (guard_location[0] + direction[0], guard_location[1] + direction[1])
        if not in_bounds(new_location, dimensions):
            guard_location = new_location
            return path

        if mx[new_location[0]][new_location[1]] == '#':
            direction_index = (direction_index + 1) % 4
            direction = directions[direction_index]
        else:
            guard_location = new_location

def count_infinite(mx: list[list[str]], dimensions: tuple[int, int]) -> int:
    path = find_path(mx, dimensions)
    count = 0
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if mx[i][j] != '#' and valid(i, j, mx, dimensions) and (i, j) not in path:
                count += 1
            mx[i][j] = '.'
    return count

def valid(i: int, j: int, mx: list[list[str]], dimensions: tuple[int, int]) -> bool:
    guard_location = find_guard(mx, dimensions)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    direction = directions[direction_index]

    mx[i][j] = '#'
    turn = 0
    turns = [None, None, None, None]

    while in_bounds(guard_location, dimensions):
        new_location = (guard_location[0] + direction[0], guard_location[1] + direction[1])
        if not in_bounds(new_location, dimensions):
            return False

        if mx[new_location[0]][new_location[1]] == '#':
            direction_index = (direction_index + 1) % 4
            direction = directions[direction_index]
            if mx[guard_location[0]][guard_location[1]] in turns:
                return True
            turns[turn] = (guard_location[0], guard_location[1])
            turn = (turn + 1) % 4
        else:
            guard_location = new_location

def main():    
    matrix = build_matrix()
    dimensions = len(matrix), len(matrix[1])

    print(f"Day six part one: {sum(map(lambda r: sum(map(lambda v: 1 if v == 'X' else 0,r)), move_guard(matrix, dimensions)))}")
    matrix = build_matrix()
    print(f"Day six part two: {count_infinite(matrix, dimensions)}")

main()