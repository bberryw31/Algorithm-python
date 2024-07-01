import sys

N = int(sys.stdin.readline())
Nlist = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mlist = list(map(int,sys.stdin.readline().split()))
result = [0]*20000001
for num in Nlist:
    result[10000000+num]+=1
result2 = []
for num in Mlist:
    result2.append(result[10000000+num])
print(" ".join(str(r) for r in result2))
