import numpy as np

def build_matrix() -> list[list[str]]:
    with open("input.txt") as f:
        return [list(line.strip()) for line in f.readlines()]
matrix = np.array(build_matrix())
dimensions = matrix.shape
WORD = "XMAS"

def search() -> tuple[int,int]:
    occurrences1 = 0
    occurrences2 = 0
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if matrix[i,j] == WORD[0]:
                occurrences1 += search_around(i, j)
            if matrix[i,j] == 'A':
                occurrences2 += search_around(i, j)
    return (occurrences1, occurrences2)

def search_around(i, j) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    if matrix[i,j] != 'A': 
        for di, dj in directions:
            if check_direction(i, j, di, dj):
                count += 1
    else:
        if check_direction(i, j, -1, -1) and check_direction(i, j, -1, 1):
            count += 1
    return count

def check_direction(i, j, di, dj) -> bool:
    if matrix[i,j] != 'A': 
        for n in range(1, len(WORD)):
            ni, nj = i + n * di, j + n * dj
            if not (0 <= ni < dimensions[0] and 0 <= nj < dimensions[1]):
                return False
            if matrix[ni,nj] != WORD[n]:
                return False
    else:
        oppdi = di*-1
        oppdj = dj*-1
        if not (0 <= i+oppdi < dimensions[0] and 0 <= j+oppdj < dimensions[1] and 0 <= i+di < dimensions[0] and 0 <= j+dj < dimensions[1]):
            return False
        if not ((matrix[i+oppdi,j+oppdj] == 'M' and matrix[i+di,j+dj] == 'S') or (matrix[i+oppdi,j+oppdj] == 'S' and matrix[i+di,j+dj] == 'M')):
            return False
    return True

result = search()
print(f"Day four part one: {result[0]}")
print(f"Day four part two: {result[1]}")