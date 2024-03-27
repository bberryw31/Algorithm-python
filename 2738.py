import sys

N,M = map(int, sys.stdin.readline().split())

A = []
B = []

for i in range(N):
    input = []
    input += map(int, sys.stdin.readline().split())
    A.append(input)

for j in range(N):
    input = []
    input += map(int, sys.stdin.readline().split())
    B.append(input)

result = ""

for k in range(N):
    for l in range(M):
        result += str(A[k][l] + B[k][l]) + " "
    print(result)
    result = ""