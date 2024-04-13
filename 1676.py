import sys
import math

N = int(sys.stdin.readline())
X = []
X.extend(str(math.factorial(N)))
count = 0
for i in range(len(X)-1,0,-1):
    if X[i] == "0":
        count +=1
    else:
        break
print(count)