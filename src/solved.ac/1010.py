T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    a = 1
    b = 1
    for j in range(N):
        a = a * (M-j)
        b = b * (j+1)
    print(a//b)

