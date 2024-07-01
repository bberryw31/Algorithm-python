import sys

N = sys.stdin.readline().strip()
result = []

if int(N)-9*len(N) < 0:
    start = 0
else:
    start = int(N)-9*len(N)

for i in range(start,int(N)):
    a = i
    for num in str(i):
        a += int(num)
    if a == int(N):
        result.append(i)

if len(result) == 0:
    print(0)
else:
    print(min(result))