import sys
input = sys.stdin.readline

N = int(input())
nums = []
sum = 0
count = [[0,int(x)] for x in range(-4000,4001)]
max = -4000
min = 4000
for i in range(N):
    num = int(input())
    nums.append(num)
    sum += num
    count[num+4000][0] += 1
    if num>max:
        max = num
    if num<min:
        min = num
print(round(sum/N))
nums_srt = sorted(nums)
print(nums_srt[N//2])
count.sort(key=lambda x:-x[0])
if count[0][0]>count[1][0]:
    print(count[0][1])
else:
    print(count[1][1])
print(max-min)