import sys
import math
from collections import defaultdict, deque
item = {}
inn = defaultdict(list)
state = defaultdict(int)
have = defaultdict(set)


want = ['gv', 'll', 'qf', 'rc']
cycle = defaultdict(list)

def bfs(i):
    q = deque()

    # node, signal, parent
    q.append(("broadcaster", 0, "button"))
    
    while len(q):
        (node, signal, par) = q.popleft()
        if node not in item: continue
        [kind, adj] = item[node]
        if kind == 'broadcaster':
            for nxt in adj:
                q.append((nxt, signal, node))
            continue
        
        if kind == '%':
            if signal == 1: continue
            state[node] ^= 1
            for nxt in adj:
                q.append((nxt, state[node], node))
            continue
        
        if kind == '&':
            if par in have[node]:
                have[node].remove(par)
            if signal == 1:
                have[node].add(par)
            if len(have[node]) == len(inn[node]):
                state[node] = 0
            else:
                state[node] = 1
                
            if node in want and state[node] == 0:
                cycle[node].append(i)

            for nxt in adj:
                q.append((nxt, state[node], node))
        continue
    return False

nodes = set()

for s in sys.stdin:
    node, nxt = s.strip().split(' -> ')
    kind = 'broadcaster'
    if node[0]== '%':
        kind ='%'
        node = node[1:]
    elif node[0] == '&':
        kind = '&'
        node = node[1:]
    adj = []
    nodes.add(node)
    for b in nxt.split(', '):
        inn[b].append(node)
        adj.append(b)
        nodes.add(b)
    item[node] = (kind, adj)
    

for i in range(1000000000):
    bfs(i + 1)
    if len(cycle) == len(want):
        bad = False
        for a, b in cycle.items():
            if len(b) < 3: bad = True
        if bad: continue
        break

print(cycle)

lengths = []
for _, seen in cycle.items():
    lengths.append(seen[0])
    
print(math.lcm(*lengths))
    
