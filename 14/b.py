import sys
from collections import defaultdict
import copy

inn = [list(s.strip()) for s in sys.stdin]
ans = 0

def move(inn):
    prev = [0 for _ in range(len(inn[0]))]
    ans = 0
    for i, row in enumerate(inn):
        for j, r in enumerate(row):
            if r == '#':
                prev[j] = i + 1
            elif r == 'O':
                inn[i][j] = '.'
                inn[prev[j]][j] = 'O'
                prev[j] += 1 
    return inn

def rotate(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)

    return new_matrix

def score(inn):
    ans = 0
    for i, row in enumerate(inn):
        for j, r in enumerate(row):
            if r == 'O':
                ans += len(inn) - i
    return ans

m = 1000000000
seen = defaultdict(list)
grids = [inn]
for i in range(1, m): 
    for __ in range(4):
        inn = move(inn)
        inn = rotate(inn)
        
    grids.append(copy.deepcopy(inn))
    s = tuple(["".join(row) for row in inn])
    if s in seen:
        m -= i
        m %= (i - seen[s])
        inn = grids[seen[s] + m]
        break
    
    seen[s] = i

print(score(inn))