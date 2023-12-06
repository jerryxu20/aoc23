import sys
import collections

times = list(map(int, input().split(':')[-1].split()))
distances = list(map(int, input().split(':')[-1].split()))


print(times, distances)
res = 1
for a, b in zip(times, distances):
    ans = []
    for i in range(a + 1):
        speed = i
        time = a - i

        if speed * time > b:
           ans.append(i) 
    print(ans)
    res *= len(ans)
print(res)