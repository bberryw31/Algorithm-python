import sys

N = int(sys.stdin.readline())
star = "*"
for i in range(1,N+1):
    print((star*i).rjust(N))
