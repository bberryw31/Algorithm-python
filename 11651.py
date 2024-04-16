import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    nums.append((x,y))
nums_srt = sorted(nums, key=lambda x:(x[1],x[0]))
for num in nums_srt:
    print(num[0],num[1])