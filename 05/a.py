import sys
import collections

a = input()
seeds = list(map(int, a.split(':')[-1].split()))

mp = {}
current = seeds

for line in sys.stdin:
    if line.strip() == '':
        nxt = []
        for a in current:
            if a in mp:
                a = mp[a]
            nxt.append(a)
        current = nxt
        mp.clear()
        continue
    try: 
        a, b, c = map(int, line.split())
        for s in current:
            if s >= b and s < b + c:
                delta = s - b
                mp[s] = a + delta
    except:
        pass

nxt = []
for a in current:
    if a in mp:
        a = mp[a]
    nxt.append(a)
current = nxt
print(min(current))