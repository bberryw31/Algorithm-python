import sys

input = sys.stdin.readlines()

print(input)

for nums in input:
    nums = nums.strip()
    A,B = map(int,nums.split())
    print(A+B)

