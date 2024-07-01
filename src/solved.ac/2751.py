import sys

N = sys.stdin.readline()
nums = list(map(int,sys.stdin.read().splitlines()))
nums.sort()
for num in nums:
    print(num)