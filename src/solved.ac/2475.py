import sys

nums = list(map(int, sys.stdin.readline().split()))
result = 0

for num in nums:
    result += num**2

print(result%10)