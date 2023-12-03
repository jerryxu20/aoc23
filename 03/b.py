import sys

grid = [a.strip() for a in sys.stdin]
n = len(grid)
m = len(grid[0])

ans = 0 
val = [[-1 for _ in range(n)] for __ in range(m)]
nums = []
N = 0
for i in range(n):
    num = 0
    idx = []
    for j in range(m):
        if grid[i][j].isdigit():
            idx.append(j)
            num *= 10
            num += int(grid[i][j])
            continue
        for jj in idx:
            val[i][jj] = N
        if len(idx):
            N += 1
            nums.append(num)
        num = 0
        idx = []
    for jj in idx:
        val[i][jj] = N
    if len(idx):
        N += 1
        nums.append(num)

adj = [[set() for _ in range(m)] for __ in range(n)]
delta = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1]]
for i in range(n):
    for j in range(m):
        if grid[i][j] != '*': continue
        for a, b in delta:
            ii = i + a
            jj = j + b
            if ii < 0 or jj < 0 or ii >= n or jj >= m: continue
            if val[ii][jj] == -1: continue
            adj[i][j].add(val[ii][jj])                   

ans = 0
for row in adj:
    for st in row:
        if len(st) != 2: continue
        res = 1
        for i in st:
            res *= nums[i]
        ans += res
print(ans)
            