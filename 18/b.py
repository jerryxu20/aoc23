import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

def Area(corners):
    n = len(corners)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) // 2
    return area


inn = [s.strip().split() for s in sys.stdin]

poly = []
inst = []

x = 0
y = 0
extra = 0
for dir, m, c in inn:
    m = int(c[2:7].upper(), 16)
    if c[-2] == '0':
        dir = 'R'
    elif c[-2] == '1':
        dir = 'D'
    elif c[-2] == '2':
        dir = 'L'
    else:
        dir = 'U'

    if dir == 'R':
        inst.append([(0, m), dir, c])
    elif dir == 'L':
        inst.append([(0, -m), dir, c])
    elif dir == 'U':
        inst.append([(-m, 0), dir, c])
    else:
        inst.append([(m, 0), dir, c])

for delta, d, c in inst:
    extra += abs(delta[0])
    extra += abs(delta[1])
    poly.append((x, y))
    old = x
    x += delta[0]
    y += delta[1]
    
print(len(poly))
print(Area(poly) + extra//2 + 1)

