import sys
import math
from collections import defaultdict, deque

grid = [s.strip() for s in sys.stdin]
n = len(grid)
m = len(grid[0])

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(a, b, mx, strictX = True, strictY = True):
    dis = {}
    q = deque()
    q.append((a, b))
    dis[(a, b)] = 0

    while len(q):
        (i, j) = q.popleft()
        if dis[(i, j)] >= mx: break
        for a, b in delta:
            ii = i + a
            jj = j + b
            if strictY and ii != (ii % n): continue
            if strictX and jj != (jj % n): continue
            if grid[ii % n][jj % m] == '#': continue
            if (ii, jj) in dis: continue

            dis[(ii, jj)] = dis[(i, j)] + 1
            q.append((ii, jj))
    
    even = 0
    odd = 0
    for pt, d in dis.items():
        if (d % 2) == 1: odd += 1
        else: even += 1
    return (even, odd)


[fe, fo] = bfs(65, 65, 300)
[ul, _] = bfs(130, 130, 65)
[ur, _] = bfs(130, 0, 65)
[dl, _] = bfs(0, 130, 65)
[dr, _] = bfs(0, 0, 65)

[l, _] = bfs(65, 130, 130)
[r, _] = bfs(65, 0, 130)
[u, _] = bfs(130, 65, 130)
[d, _] = bfs(0, 65, 130)

[_, ull] = bfs(130, 130, 130 + 65)
[_, urr] = bfs(130, 0, 130 + 65)
[_, dll] = bfs(0, 130, 130 + 65)
[_, drr] = bfs(0, 0, 130 + 65)


ans = u + d + l + r

x = 26501365
t = (x-65)//131
ans += (ul + ur + dl + dr) * t
ans += (ull + urr + dll + drr) * (t - 1)

odd = 1
even = 0
for i in range(1, t + 1):
    ans += odd * fe
    ans += even * fo
    odd += 1
    even += 1

odd = 1
even = 0    
for i in range(1, t):
    ans += odd * fe
    ans += even * fo
    odd += 1
    even += 1
print(ans)
