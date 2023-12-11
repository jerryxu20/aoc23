import sys
import collections

grid = [line.strip() for line in sys.stdin] 

def add(grid):
    ans = [0 for _ in range(len(grid) + 1)]
    for i, row in enumerate(grid):
        ans[i + 1] = ans[i] + 1
        if '#' not in row:
            ans[i + 1] = ans[i] + 1000000
    return ans
            
    
pref_row = add(grid)
grid = list(map(list, zip(*grid)))
pref_col = add(grid)
grid = list(map(list, zip(*grid)))

gal = []
n = len(grid)
m = len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            gal.append((i, j))

ans = 0
for i in range(len(gal)):
    for j in range(i):
        x, y = gal[i]
        xx, yy = gal[j]
        if x > xx: x, xx = xx, x
        if y > yy: y, yy = yy, y

        ans += pref_row[xx] - pref_row[x] + pref_col[yy] - pref_col[y]
print(ans)