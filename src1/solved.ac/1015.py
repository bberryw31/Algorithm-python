N = input()
A = list(map(int,input().split()))

P = [] + A

smallestnum = 1001
smallest = 0

for j in range(len(A)):
    for i in range(len(A)):
        if A[i] < smallestnum:
            smallestnum = A[i]
            smallest = i
    P[smallest] = j
    A[smallest] = 1001
    smallestnum = 1001

result = ""
for k in range(len(P)):
    result = result + str(P[k]) + " "

print(result)