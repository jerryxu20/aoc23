import sys
import math
import collections
s = input()

input()

mp = {}
start = ""
for line in sys.stdin:
    a, t = line.split('=')
    a = a.strip()
    if not start: 
        start = a
    l, r = t.strip('() \n').split(',')
    l = l.strip()
    r = r.strip()
    mp[a] = (l, r)
nodes = []

for a, b in mp.items():
    if a[-1] == 'A':
        nodes.append(a)
        
def calc(node):
    Z = []
    cur = node
    ans = 0
    times = {}
    times[(node, -1)] = 0

    while True:
        for i, c in enumerate(s):
            ans += 1
            if c == 'L':
                cur = mp[cur][0]
            else:
                cur = mp[cur][1]
            if (cur, i) in times and cur[-1] == 'Z':
                Z.append(ans)
                return Z
            if cur[-1] == 'Z':
                Z.append(ans)
            times[(cur, i)] = ans
    return Z
            
# while True:
#     for c in s:
#         ans += 1
#         nnodes = []
#         for node in nodes:
#             if c == 'L':
#                 nnodes.append(mp[node][0])
#             else:
#                 nnodes.append(mp[node][1])
#         nodes = nnodes
#         good = 0
#         print(nodes)
#         for node in nnodes:
#             if node[-1] == 'Z':
#                 good += 1
#         if good == len(nodes):
#             print(ans)
#             sys.exit()
        # if cur == 'ZZZ':
        #     print(ans)
        #     sys.exit()
        # ans += 1
        # if c == 'L':
        #     cur = mp[cur][0]
        # else:
        #     cur = mp[cur][1]

ans = 1
f = []

for node in nodes:
    a = calc(node)
    f.append(a[0])
    
print(math.lcm(*f))