import sys
from collections import defaultdict


s = input()
ans = 0
def hash(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res

parts = s.split(',')
ans = 0
for p in parts:
    ans += hash(p)
print(ans)