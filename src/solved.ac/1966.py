import sys

T = int(sys.stdin.readline())
for i in range(T):
    N,M = map(int,sys.stdin.readline().split())
    queueord = list(map(int,sys.stdin.readline().split()))
    queueidx = [q for q in range(N)]
    count = 1
    while len(queueord)>0:
        if len(queueord) == 1:
            if queueidx[0] == M:
                print(count)
                break
            else:
                del queueord[0]
                del queueidx[0]
            break
        change = False
        for q in queueord[1:]:
            if queueord[0]<q:
                queueord.append(queueord.pop(0))
                queueidx.append(queueidx.pop(0))
                change = True
                break
        if change == False:
            if queueidx[0] == M:
                print(count)
                break
            else:
                del queueord[0]
                del queueidx[0]
                count +=1