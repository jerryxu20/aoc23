import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
inn = [s.strip() for s in sys.stdin]
n = len(inn)
m = len(inn[0])

valid = [[False for _ in range(m)] for __ in range(m)]
seen = set()

def nxt(dir, tile):
    if tile == '.': return [dir]

    up, down, left, right = False, False, False, False
    if dir == (1, 0): down = True
    if dir == (-1, 0): up = True
    if dir == (0, -1): left = True
    if dir == (0, 1): right = True

    if (left or right) and tile == '-': return [dir]
    if (up or down) and tile == '|': return [dir]


    if (left or right) and tile == '|': return [(-1, 0), (1, 0)]
    if (up or down) and tile == '-': return [(0, -1), (0, 1)] 


    if left and tile == '/': return [(1, 0)]
    if right and tile == '/': return [(-1, 0)]
    
    if up and tile == '/': return [(0, 1)]
    if down and tile == '/': return [(0, -1)]
    
    assert tile == '\\'
    
    if left and tile == '\\':  return [(-1, 0)]
    if right and tile == '\\': return [(1, 0)]
    
    if up and tile == '\\': return [(0, -1)]
    if down and tile == '\\': return [(0, 1)]

    assert False
    return    

dp = {}
bad = set()
def dfs(i, j, dir):
    state = (i, j, dir)
    if state in seen: return 
    seen.add(state)
    bad.add(state)
    if state in dp: 
        table = dp[state]
        for ii in range(n):
            for jj in range(m):
                valid[ii][jj] |= table[ii][jj]
        return

    if i < 0 or j < 0 or i >= n or j >= m: return 
    valid[i][j] = True
    dirs = nxt(dir, inn[i][j])
    for d in dirs:
        dfs(i + d[0], j + d[1], d)
    return
    
ans = 0
for i in range(n):
    for j in range(m):
        for dir in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            if (i, j, dir) in bad: continue
            valid = [[False for _ in range(m)] for __ in range(m)]
            
            seen.clear()
            dfs(i,j,dir)
            cand = 0
            for row in valid:
                cand += row.count(True)
            ans = max(ans, cand)
            dp[(i, j, dir)] = tuple(map(tuple, valid))
print(ans)