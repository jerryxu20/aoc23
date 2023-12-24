import sys
from z3 import *

S = Solver()
x = Int('x')
y = Int('y')
z = Int('z')
dx = Int('dx')
dy = Int('dy')
dz = Int('dz')

for i, s in enumerate(sys.stdin):
    a, b = s.strip().split('@')
    p = tuple(map(int, a.split(',')))
    d = tuple(map(int, b.split(',')))
    
    t = Int(str(i))
    S.add(x + t * dx == p[0] + t * d[0], t > 0)
    S.add(y + t * dy == p[1] + t * d[1], t > 0)
    S.add(z + t * dz == p[2] + t * d[2], t > 0)

S.check()
m = S.model()
print(m[x].as_long() + m[y].as_long() + m[z].as_long())