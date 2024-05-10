import sys
import math
input = sys.stdin.readline

N,M,B = map(int,input().split())
a = []
for i in range(N):
    a += list(map(int,input().split()))
minheight = min(a)
maxheight = max(a)
b = [int(x) for x in range(minheight,maxheight+1)]
c = []
for bl in b:
    c.append([bl, a.count(bl)])

result = []
mintime = math.inf
for height in b:
    time,block = 0,0
    for x in c:
        if x[0] == height:
            continue
        else:
            if x[0]<height:
                block-=x[1]*(height-x[0])
                time+=x[1]*(height-x[0])
            else:
                block+=x[1]*(x[0]-height)
                time+=x[1]*2*(x[0]-height)
    if B+block>=0:
        if time<mintime:
            mintime = time
            result = [[height,time]]
        elif time==mintime:
            result.append([height,time])

result.sort(key=lambda x:-x[0])
print(result[0][1], result[0][0])