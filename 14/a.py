import sys
from collections import defaultdict


inn = [list(s.strip()) for s in sys.stdin]

ans = 0
prev = [0 for _ in range(len(inn[0]))]

for i, row in enumerate(inn):
    for j, r in enumerate(row):
        if r == '#':
            prev[j] = i + 1
        elif r == 'O':
            inn[i][j] = '.'
            inn[prev[j]][j] = 'O'
            ans += len(inn) - prev[j]
            prev[j] += 1 
print(ans)