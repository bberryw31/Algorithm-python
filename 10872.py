N = int(input())
result = N
if N == 0:
    print(1)
else:
    for i in range(1,N):
        result = result * (N-i)
    print(result)
