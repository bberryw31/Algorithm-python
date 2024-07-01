import sys

N = int(sys.stdin.readline())

nums = []
for i in range(N):
    newnum = int(sys.stdin.readline())
    if newnum == 0 and len(nums)>0:
        del nums[-1]
    else:
        nums.append(newnum)
print(sum(nums))