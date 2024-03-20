import sys
sys.setrecursionlimit(10000)

def joiner(q):
    origin = [coor[q][0], coor[q][1]]
    compare1 = [coor[q][0]-1, coor[q][1]] #좌
    compare2 = [coor[q][0], coor[q][1]-1] #상
    compare3 = [coor[q][0]+1, coor[q][1]] #우
    compare4 = [coor[q][0], coor[q][1]+1] #하
    join.append(origin)
    coor.remove(origin)

    if compare1 in coor and compare1 not in join:
        joiner(coor.index(compare1))
    if compare2 in coor and compare2 not in join:
        joiner(coor.index(compare2))
    if compare3 in coor and compare3 not in join:
        joiner(coor.index(compare3))
    if compare4 in coor and compare4 not in join:
        joiner(coor.index(compare4))

T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    coor = []
    for j in range(K):
        a, b = map(int, input().split())
        X = [a, b]
        coor.append(X)

    result = []
    counter = 0

    while len(coor)>0:
        join = []
        joiner(0)
        result.append(join)

    print(len(result))
