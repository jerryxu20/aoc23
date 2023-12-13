import sys
from collections import defaultdict


grid = []

ans = 0

def solve(grid):
    print(grid)
    print()
    # agree for all rows
    cnt = defaultdict(int)
    for row in grid:
        for i in range(1, len(row)):
            l = min(i, len(row) - i)
            left = row[i-l:i]
            right = row[i:i+l]
            right = right[::-1]
            if left == right:
                cnt[i] += 1
        
    ans = 0
    for i, c in cnt.items():
        if c == len(grid):
            ans += i
    return ans

inn = [s.strip() for s in sys.stdin]
inn.append("")

for s in inn:
    if not s:
        ans += solve(grid)
        grid = list(map(list, zip(*grid)))
        grid.reverse()
        ans += 100 * solve(grid)
        grid = []
        continue
    grid.append(list(s))
print(ans)


