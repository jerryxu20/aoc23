import sys
import collections

ans = 0

def solve(v):
    zero = True
    for d in v:
        if d != 0: zero = False        
    if zero:
        return 0

    delta = []
    for i in range(1, len(v)):
        delta.append(v[i] - v[i - 1])
    b = solve(delta)
    return b + v[-1]

for line in sys.stdin:
    a = list(map(int, line.split()))
    a = a[::-1]
    ans += solve(a)
print(ans)