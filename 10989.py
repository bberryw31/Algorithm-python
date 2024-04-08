import sys

N = int(sys.stdin.readline())
temp = [0]*10001
for l in range(N):
    temp[int(sys.stdin.readline())]+=1
for i in range(10001):
    for j in range(temp[i]):
        print(i)