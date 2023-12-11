import sys
import collections

grid = [line.strip() for line in sys.stdin]
        
def add(grid):
    ans = []
    for line in grid:
        ans.append(line)
        if '#' not in line:
            ans.append(line)
    return ans

    
grid = add(grid)
grid = list(map(list, zip(*grid)))
grid = add(grid)
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
        ans += abs(x - xx) + abs(y - yy)
print(ans)