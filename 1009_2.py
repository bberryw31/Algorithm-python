result = []

T = int(input())

for j in range(T):
    X = input().split()
    a = int(X[0])
    b = int(X[1])

    c = a

    for i in range(b - 1):
        c = c * a

    result.append(c % 10)

for k in range(T):
    print(result[k])