def read_lines() -> list[str]:
    with open("lists.txt") as f:
        return f.readlines()

def create_tuples() -> list[tuple[int, int]]:
    lines = read_lines()
    return list(map(lambda l : tuple(l.split("   ")), lines))

def unzip(pairs: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for pair in pairs:
        left.append(int(pair[0]))
        right.append(int(pair[1]))
    return left, right

left, right = unzip(create_tuples())
left.sort()
right.sort()

print(f"Day one part one: {sum(map(lambda t : abs(t[0] - t[1]), zip(left, right)))}")

print(f"Day one part two: {sum(map(lambda l : (l * right.count(l)), left))}")
