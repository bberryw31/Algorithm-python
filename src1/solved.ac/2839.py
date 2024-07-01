import sys

N = int(sys.stdin.readline())
result = []
for i in range((N//5)+1):
    if (N-(5*i))%3==0:
        result.append((i,(N-(5*i))/3))

if len(result)==0:
    print(-1)
else:
    print(int(result[-1][0]+result[-1][1]))