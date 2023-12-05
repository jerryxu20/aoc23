import sys
import collections

a = input()
seeds = list(map(int, a.split(':')[-1].split()))

current = []
nxt = []
for i in range(0, len(seeds), 2):
    current.append((seeds[i], seeds[i] + seeds[i + 1]-1))
    
for line in sys.stdin:
    if line.strip() == '':
        for a in nxt:
            current.append(a)
        nxt = []
    try: 
        a, b, c = map(int, line.split())
        v = []
        high = b + c - 1
        low = b
        for x, y in current:
            if x > high or y < low:
                v.append((x, y)) 
                continue
            if x < low:
                v.append((x, low - 1))
                x = low
            
            if y > high:
                v.append((high + 1, y))
                y = high
            delta = x - b
            nxt.append((a + delta, a + delta + (y - x)))
        current = v
    except:
        pass

for a in nxt:
    current.append(a)
    
print(min(current)[0])