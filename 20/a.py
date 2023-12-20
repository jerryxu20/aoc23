import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10 ** 6)
item = {}
inn = defaultdict(list)
state = defaultdict(int)
have = defaultdict(set)
low = 0
high = 0

def bfs():
    global low, high
    q = deque()
    q.append(('broadcaster', 0, 'button'))
    
    while len(q):
        (node, signal, par) = q.popleft()
        if node == 'rx' and signal == 0: return True
        if signal == 0: low += 1
        else: high += 1
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
            for nxt in adj:
                q.append((nxt, state[node], node))
        continue
        
    return False

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
    for b in nxt.split(', '):
        inn[b].append(node)
        adj.append(b)
    item[node] = (kind, adj)
    


for i in range(1000):
    bfs()
print(low, high)
print(low * high)