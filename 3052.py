import sys

nums = list(map(int,sys.stdin.read().splitlines()))
res = set()
for num in nums:
    res.add(num%42)
print(len(res))