import sys

def prime(x):
    list = []
    i = 2
    while i<=x or x>1:
        if x%i==0:
            list.append(i)
            x = x/i
        else:
            i+=1
    return list

A,B = map(int,sys.stdin.readline().split())
if A==1 or B==1:
    print(1)
    print(max(A,B))
    exit()
al,bl = prime(A),prime(B)
X,Y = 1,1
for num in set(al+bl):
    Y = Y*(num**max(al.count(num),bl.count(num)))
    if num in al and bl:
        X = X*(num**min(al.count(num),bl.count(num)))

print(X)
print(Y)