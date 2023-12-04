import sys
import collections


ans = 0

for i, s in enumerate(sys.stdin):
    s = s.strip()
    want, have = s.split('|')
    want = want.split(':')[-1]
    want = list(map(int, want.split()))
    have = list(map(int, have.split()))

    wins = 0
    for c in have:
        if c in want:
            wins += 1
    if wins == 0: continue
    ans += 1 << (wins - 1)
    
print(ans)