import sys
ans = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in sys.stdin:
    nums = []
    for i, c in enumerate(line):
        try:
            c = int(c)
            nums.append(c)
        except:
            pass
    a = int(str(nums[0]) + str(nums[-1]))
    ans += a
print(ans)