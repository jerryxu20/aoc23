import sys
import collections


grid = [s.strip() for s in sys.stdin]

def ccount(arr):
    run = 0
    ans = []
    arr.append(0)
    for thing in arr:
        if thing == 1:
            run += 1
        else:
            if run > 0:
                ans.append(run)
            run = 0
    return ans
def ways(s, arr):
    seen = set()
    n = len(s)
    ans = 0
    for i in range(1 << n):
        perm = []
        for j in range(n):
            if s[j] == '?':
                a = (i & (1 << j)) > 0
                perm.append(a)
            elif s[j] == '#':
                perm.append(1)
            else:
                perm.append(0)
        if tuple(perm) in seen: continue
        seen.add(tuple(perm))
        if ccount(perm) == arr:
            ans += 1
    return ans 
ans = 0
for s in grid:
    a, b = s.split()
    b = list(map(int, b.split(',')))

    ans += ways(a, b)
    print(a, b, ans)
print(ans)