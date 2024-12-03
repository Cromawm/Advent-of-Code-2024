import re

def read_lines() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()

mulPattern = r'mul\(\d{1,3},\d{1,3}\)'
doPattern = r'do\(\)'
dontPattern = r'don\'t\(\)'
combinedPattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'

numPattern = r'\d{1,3}'

def find_matches() -> list[str]:
    return [match.group(0) for line in read_lines() for match in re.finditer(combinedPattern, line)]

def find_valid() -> list[str]:
    allMatches = find_matches()
    valid = []
    dontFlag = False
    for match in allMatches:
        if re.match(mulPattern, match) and not dontFlag:
            valid.append(match)
        elif re.match(doPattern, match):
            dontFlag = False
        elif re.match(dontPattern, match):
            dontFlag = True
    return valid

def apply_mul(mul: str) -> int:
    (a,b) = re.findall(numPattern, mul)
    return int(a) * int(b)

def apply_all() -> int:
    return sum(map(apply_mul, find_valid()))

print(apply_all())
