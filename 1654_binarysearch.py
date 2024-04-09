import sys

def cut(bt,tp):
    if tp-bt!=1:
        count = 0
        for line in lines:
            count += line//((bt+tp)//2)
        if count >= N:
            cut((bt+tp)//2,tp)
            result.append((bt+tp)//2)
        else:
            cut(bt,(bt+tp)//2)
    else:
        count = 0
        for line in lines:
            count += line//((bt+tp)//2+1)
        if count >= N:
            result.append((bt+tp)//2+1)
K,N = map(int,sys.stdin.readline().split())
lines = []
for i in range(K):
    lines.append(int(sys.stdin.readline()))

result = []
bot = 0
top = max(lines)

if N==K==1:
    print(lines[0])
else:
    cut(bot,top)
    print(max(result))