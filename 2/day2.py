def read_lines() -> list[str]:
    with open("lists.txt") as f:
        return f.readlines()

def parse_record(record: str) -> list[int]:
    return list(map(int, record.split(" ")))

def parse_records() -> list[list[int]]:
    return list(map(parse_record, read_lines()))

def adj(l:list[any]) -> list[tuple[any, any]]:
    return list(zip(l, l[1:]))

def increasing(l: list[int]) -> bool:
    return all(x > y for (x, y) in adj(l))

def decreasing(l: list[int]) -> bool:
    return all(x < y for (x, y) in adj(l))

def adjacent(l: list[int]) -> bool:
    return all(4 > abs(x-y) for (x, y) in adj(l))

def is_safe (l: list[int]) -> bool:
    return (increasing(l) or decreasing(l)) and adjacent(l)

def count_safe() -> int:
    return len(list(filter(is_safe, parse_records())))

print(f"Day two part one: {count_safe()}") 

def is_safe_dampened(l: list[int]) -> bool:
    return is_safe(l) or any(list(map(is_safe, [l[:i] + l[i+1:] for i in range(len(l))])))

def count_safe_dampened() -> int:
    return len(list(filter(is_safe_dampened, parse_records())))

print(f"Day two part two: {count_safe_dampened()}")
    



# lmao we can write it as one line
# with open("lists.txt") as f: print(f"Day two part one: {len(list(filter(lambda l: (all(x > y for (x, y) in list(zip(l, l[1:]))) or all(x < y for (x, y) in list(zip(l, l[1:])))) and all(4 > abs(x-y) for (x, y) in list(zip(l, l[1:]))), list(map(lambda r: list(map(int, r.split(" "))), f.readlines())))))}")