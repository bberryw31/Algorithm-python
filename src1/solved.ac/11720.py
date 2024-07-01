import sys

N = int(sys.stdin.readline())
nums = sys.stdin.readline().strip()
result = 0
for num in nums:
    result += int(num)
print(result)