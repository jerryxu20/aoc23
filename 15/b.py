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
mp = defaultdict(list)
val = defaultdict(int)
for p in parts:
    label = ""
    op = ""
    focal = ""
    try:
        label, op = p.split('-')
        op = '-'
    except:
        label, focal = p.split('=')
        op = '='
    box = hash(label)
    if op == '-':
        try:
            mp[box].remove(label)
        except:
            pass
        continue
    if label not in mp[box]:
        mp[box].append(label)
    val[label] = int(focal)
    
ans = 0
for i, box in mp.items():
    for j, item in enumerate(box):
        ans += (i + 1) * (j + 1) * val[item]
print(ans)