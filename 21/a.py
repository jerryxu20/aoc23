import sys
from collections import defaultdict, deque

grid = [s.strip() for s in sys.stdin]
n = len(grid)
m = len(grid[0])
dis = [[1e9 for _ in range(m)] for __ in range(n)]

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    dis[a][b] = 0

    while len(q):
        (i, j) = q.popleft()
        for a, b in delta:
            ii = i + a
            jj = j + b
            if ii < 0 or jj < 0 or ii >= n or jj >= m or grid[ii][jj] != '.': continue
            if dis[ii][jj] != 1e9: continue
            dis[ii][jj] = dis[i][j] + 1
            q.append((ii, jj))
    return
    
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            bfs(i, j)
            break

ans = 0
for i in range(n):
    for j in range(m):
        if dis[i][j] <= 64 and dis[i][j] % 2 == 0:
            ans += 1
print(ans)