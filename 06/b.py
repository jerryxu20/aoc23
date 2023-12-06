import sys
import collections

times = input().split(':')[-1].replace(' ', '')
distances = input().split(':')[-1].replace(' ', '')

times = int(times)
distances = int(distances)

def check(a):
    rem = times - a
    return a * rem > distances
    
low = 0
high = times
a1 = 0
while low <= high:
    mid = (low + high) //2
    if check(mid):
        high = mid - 1  
        a1 = mid
    else:
        low = mid + 1

low = 0
high = times
a2 = high
while low <= high:
    mid = (low + high) //2
    if check(mid):
        low = mid + 1
        a2 = mid
    else:
        high = mid - 1
print(a1, a2)
print(a2 - a1 + 1)