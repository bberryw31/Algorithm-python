import sys

N = int(sys.stdin.readline())

x = 1
N -= 1
if N == 0:
    print(x)
else:
    while True:
        N = N - 6*x
        if N > 0:
            x += 1
        else:
            x += 1
            print(x)
            exit()