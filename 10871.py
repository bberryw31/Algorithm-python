import sys

A, X = map(int, sys.stdin.readline().split())
Alist = []
Alist += map(int, (sys.stdin.readline().split()))
result = ""
for item in Alist:
    if item < X:
        result += str(item) + " "

print(result)