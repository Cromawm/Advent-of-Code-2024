from itertools import product

def read_lines() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()
    
def parse_record(record: str) -> list[int]:
    return list(record.split(": "))

def parse_records() -> list[list[int]]:
    return list(map(parse_record, read_lines()))

def permutations(ops, line) -> list[list[int]]:
    return list(product(ops, repeat=(len(line)-1)))

def apply(line, permutation) -> int:
    result = line[0]
    for i, operation in enumerate(permutation):
        result = {'*': lambda x, y: x * y, '+': lambda x, y: x + y, '||': lambda x, y: int(str(x)+str(y))}[operation](result, line[i + 1])
    return result

def calculate_total(ops) -> int:
    total = 0
    lines = parse_records()
    for line in lines:
        expected = int(line[0])
        vals = list(map(int, line[1:][0].split(" ")))
        for perm in permutations(ops, vals):
            if apply(vals, perm) == expected:
                total += expected
                break
    return total

def part_one() -> int:
    return calculate_total(['*','+'])

def part_two() -> int:
    return calculate_total(['*','+','||'])

print(f"Day seven part one: {part_one()}")
print(f"Day seven part two: {part_two()}")