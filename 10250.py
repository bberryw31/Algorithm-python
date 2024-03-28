import sys
for i in range(int(sys.stdin.readline())):
    H,W,N = map(int,sys.stdin.readline().split())
    if N%H == 0:
        X = N//H
        Y = H
    else:
        X = N//H +1
        Y = N%H

    if X<10:
        X = "0" + str(X)
    else:
        X = str(X)
    Y = str(Y)
    print(Y+X)
