import sys
import collections


ans = 0
cur = 1
sub = [0 for _ in range(1000)]

for i, s in enumerate(sys.stdin):
    cur -= sub[i]
    ans += cur
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
    sub[min(i + wins + 1, 999)] += cur
    cur += cur
    
print(ans)