import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
result = A*B*C
nums = []
nums.extend(str(result))
for i in range(10):
    print(nums.count(str(i)))