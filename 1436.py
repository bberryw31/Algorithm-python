import sys

def number(n): #n = 2
    for y in range(n+1): #y = 0,1,2
        x = n-y #2,1,0
        if x>0:
            for prefix in range(10**(x-1),10**x): #두자릿수 prefix
                if y>0:
                    for suffix in range(10**y):
                        nums.append(int(str(prefix) + "666" + "0"*(len(str(10**y))-1-len(str(suffix))) + str(suffix)))
                else:
                    nums.append(int(str(prefix) + "666"))
        else:
            for suffix in range(10**y):
                nums.append(int("666" + "0"*(len(str(10**y))-1-len(str(suffix))) + str(suffix)))

N = int(sys.stdin.readline().strip())

if N == 1:
    print(666)
else:
    N = N-1
    digit = 1
    while True:
        result, nums = [], []
        number(digit)
        result = list(set(nums))
        result.sort()
        if N>len(result):
            digit += 1
            N -= len(result)
        else:
            print(result[N-1])
            exit()