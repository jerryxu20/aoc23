import sys
mp = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def good(s):
    g = s.split(',')
    for item in g:
        n, c = item.split()
        n = int(n)
        if n > mp[c]: return False
    return True

ans = 0
for i, line in  enumerate(sys.stdin):
    _, g = line.strip().split(': ')
    games = g.split(';')
    res = [1 for game in games if good(game)]
    if len(res) == len(games):
        ans += i + 1
print(ans)    
