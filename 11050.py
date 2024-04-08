import sys
import math

N,K = map(int,sys.stdin.readline().split())
print(int(math.factorial(N)/math.factorial(N-K)/math.factorial(K)))