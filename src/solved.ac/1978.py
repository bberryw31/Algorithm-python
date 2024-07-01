import sys

N = sys.stdin.readline()
nums = list(map(int, sys.stdin.readline().split()))
primecount = 0
for num in nums:
    isprime = True
    if num != 1:
        for i in range(2,num):
            if num%i == 0:
                isprime = False
        if isprime == True:
            primecount += 1

print(primecount)