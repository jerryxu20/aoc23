import sys
ans = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in sys.stdin:
    nums = []
    for i, c in enumerate(line):
        try:
            c = int(c)
            nums.append([i, c])
        except:
            pass
    for i, d in enumerate(digits):
        idx = line.find(d)
        if idx != -1: nums.append([idx, i + 1])
        idx = line.rfind(d)
        if idx != -1: nums.append([idx, i + 1])
    
    nums.sort()
    a = int(str(nums[0][1]) + str(nums[-1][1]))
    ans += a
print(ans)