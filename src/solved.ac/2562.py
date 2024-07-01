import sys

nums = list(map(int, sys.stdin.read().splitlines()))
nums_o = [] + nums
nums.sort()

print(nums[len(nums)-1])
print(nums_o.index(nums[len(nums)-1])+1)