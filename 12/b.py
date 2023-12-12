import sys
import collections


grid = [s.strip() for s in sys.stdin]

dp = {}

def ways(s, arr):

    while s and s[-1] == '.':
        s.pop()

    if not s and not arr: 
        return 1       
    if not s and arr: return 0
    
    a = tuple(s)
    b = tuple(arr)
    state = tuple([len(a), len(arr)])    
    if state in dp:
        return dp[state]

    ans = 0
    if s[-1] == '?':
        ans += ways(s[:-1], arr[:])
    if not arr:
        dp[state] = ans
        return ans
    targ = arr[-1]
    while targ > 0:
        if not s or s[-1] == '.': 
            dp[state] = ans
            return ans
        s.pop()
        targ -= 1
    
    if s and s[-1] == '#':
        dp[state] = ans
        return ans
    if s and s[-1] == '?':
        s.pop()
    ans += ways(s[:], arr[:-1])
    dp[state] = ans
    return ans
    
    
ans = 0
for s in grid:
    a, b = s.split()
    b = list(map(int, b.split(',')))

    actual = []
    arr = []
    for _ in range(5):
        actual += a
        actual.append('?')
        arr += b
    actual.pop()
    dp.clear()
    print(ans)
    ans += ways(actual, arr)
print(ans)