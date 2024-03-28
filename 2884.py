import sys
A,B = map(int, sys.stdin.readline().split())

if B<45:
    if A==0:
        A = 23
        B += 15
    else:
        A -= 1
        B += 15
else:
    B -= 45

print(A,B)