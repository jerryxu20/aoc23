import sys
import math
import collections
s = input()

input()

mp = {}
start = ""
for line in sys.stdin:
    a, t = line.split('=')
    a = a.strip()
    if not start: 
        start = a
    l, r = t.strip('() \n').split(',')
    l = l.strip()
    r = r.strip()
    mp[a] = (l, r)
        
ans = 0
cur = "AAA"
while True:
    for c in s:
        if cur == 'ZZZ':
            print(ans)
            sys.exit()
        ans += 1
        if c == 'L':
            cur = mp[cur][0]
        else:
            cur = mp[cur][1]
