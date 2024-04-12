import sys

N = int(sys.stdin.readline())
nums = {}
keys = []
for i in range(N):
    X,Y = map(int,sys.stdin.readline().split())
    if X in nums:
        nums[X].append(Y)
    else:
        nums[X] = [Y]
        keys.append(X)

keys.sort()

for key in keys:
    values = nums[key]
    values.sort()
    for value in values:
        print(str(key) + " " + str(value))

