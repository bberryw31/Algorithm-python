import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
print(str(nums[0]) + " " + str(nums[len(nums)-1]))