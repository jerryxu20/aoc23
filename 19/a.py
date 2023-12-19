import sys

workflows = {}
queries = []
inn = []
ans = 0

def dfs(mp, s):
    if s == 'A': 
        res = 0
        for a, b in mp.items():
            res += b
        return res
    if s == 'R': return 0
    assert s in workflows

    for sign, x, val, nxt in workflows[s]:
        if sign == 'x':
            return dfs(mp, nxt)
        if sign == '>' and mp[x] > val:
            return dfs(mp, nxt)
        if sign == '<' and mp[x] < val:
            return dfs(mp, nxt)
    assert False
    return 0

for s in sys.stdin:
    s = s.strip()
    if not s: break
    name, rest = s.split('{')
    parts = rest[:-1].split(',')
    flow = []
    for part in parts:
        try: 
            cond, nxt = part.split(':')
            x = cond[0]
            sign = cond[1]
            val = int(cond[2:])
        except:
            nxt = part
            sign = 'x'
            val = 0
        flow.append((sign, x, val, nxt))
    workflows[name] = flow
    
for s in sys.stdin: 
    mp = {}
    for part in s.strip()[1:-1].split(','):
        var, val = part.split('=')
        val = int(val)
        mp[var] = val       
    queries.append(mp)

for q in queries:
    ans += dfs(q, 'in')
print(ans)