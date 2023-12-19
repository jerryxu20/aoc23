import sys

workflows = {}
queries = []
inn = []
ans = 0

def dfs(mp, s):
    global ans
    if s == 'A': 
        res = 1
        for _, a in mp.items():
            res *= a[1] - a[0] + 1
        ans += res
        return
        
    if s == 'R': return 0
    assert s in workflows

    for sign, x, val, nxt in workflows[s]:
        new_mp = mp.copy()
        if sign == 'x':
            dfs(mp, nxt)
            return
        low, high = mp[x]
        if sign == '>' and high > val:
            new_mp[x] = [max(low, val + 1), high]
            dfs(new_mp, nxt)
            if low > val: return
            mp[x] = [low, min(val, high)]

        if sign == '<' and low < val:
            new_mp[x] = [low, min(val - 1, high)]
            dfs(new_mp, nxt)
            if high < val: return
            mp[x] = [max(low, val), high]
    return

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
            x = '5'
            val = 0
        flow.append((sign, x, val, nxt))
    workflows[name] = flow


mp = {
    'x': [1, 4000],
    'm': [1, 4000],
    'a': [1, 4000],
    's': [1, 4000],
}

dfs(mp, 'in')
print(ans)