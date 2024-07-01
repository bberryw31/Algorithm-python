import sys

N = int(sys.stdin.readline())
A = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
for num in B:
    if num in A:
        print(1)
    else:
        print(0)
