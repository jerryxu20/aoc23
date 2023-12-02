import sys
def min_count(game):
    mp = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for g in game:
        for item in g.split(','):
            n, c = item.split()
            n = int(n)
            mp[c] = max(mp[c], n)
    return (mp["red"], mp["blue"], mp["green"])

ans = 0
for i, line in  enumerate(sys.stdin):
    _, g = line.strip().split(': ')
    games = g.split(';')
    a, b, c = min_count(games)
    ans += a * b * c        
print(ans)

      