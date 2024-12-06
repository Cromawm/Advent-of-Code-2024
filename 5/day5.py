rule_type = dict[str, set[list[str]]] 

def parse_input() -> tuple[rule_type, list[list[str]]]:
    with open("./5/input.txt") as f:
        lines = f.read().splitlines()
        split_index = lines.index("")
        rules = parse_rules(list(map(lambda line: tuple(line.split("|")), lines[:split_index])))
        book = list(map(lambda line: line.split(","), lines[split_index+1:]))
    return rules, book

def parse_rules(rules: list[tuple[str,str]]) -> rule_type:
    rules_set:rule_type = {}
    for (smaller, larger) in rules:
        if smaller not in rules_set.keys(): rules_set[smaller] = set()
        rules_set[smaller].add(larger)
    return rules_set

def check_pages(rules: rule_type, line: list[str]) -> bool:
    for i, val in enumerate(line):
        for val2 in line[i+1:]:
            if val in rules.get(val2): return False
    return True  

def part_one() -> int:
    rules, book = parse_input()
    valids = list(filter(lambda page: check_pages(rules, page), book))
    return sum(map(lambda page: int(page[len(page)//2]), valids))

def part_two() -> int:
    rules, book = parse_input()
    invalids = list(map(lambda page: sort(rules, page), filter(lambda page: not check_pages(rules, page), book)))
    return sum(map(lambda page: int(page[len(page)//2]), invalids))

def sort(rules: rule_type, line) -> list[str]:
    sorted = []
    for val in line:
        for i, val2 in enumerate(sorted):
            if val2 in rules.get(val):
                sorted.insert(i, val)
                break
        else:
            sorted.append(val)
    return sorted

print(f"Day five part one: {part_one()}")
print(f"Day five part two: {part_two()}")