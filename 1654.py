import sys

K,N = map(int,sys.stdin.readline().split())
lines = []
for i in range(K):
    lines.append(int(sys.stdin.readline()))
max = sum(lines)//N
for j in range(max):
    count = 0
    for line in lines:
        count += line//(max-j)
    if count >= N:
        print(max-j)
        exit()