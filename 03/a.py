import sys

grid = [a.strip() for a in sys.stdin]

n = len(grid)
m = len(grid[0])

valid = [[False for _ in range(m)] for __ in range(n)]

delta = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1]]
for i in range(n):
    for j in range(m):
        if grid[i][j].isdigit() or grid[i][j] == '.': continue
        for a, b in delta:
            ii = i + a
            jj = j + b
            if ii < 0 or jj < 0 or ii >= n or jj >= m: continue
            valid[ii][jj] = True

ans = 0 
for i in range(n):
    num = 0
    inc = False
    for j in range(m):
        if grid[i][j].isdigit():
            if valid[i][j]: inc = True
            num *= 10
            num += int(grid[i][j])
            continue
        if inc:
            ans += num
        num = 0
        inc = False
    if inc:
        ans += num
print(ans)
            