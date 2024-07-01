import sys

nums = []
nums += map(int, sys.stdin.readlines())

for i in range(1,31):
    if i not in nums:
        print(i)