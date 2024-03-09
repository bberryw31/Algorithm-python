def entail(a1, b1, a2, b2, r):
    if (a1-a2)**2 + (b1-b2)**2 < r**2:
        return True
    else:
        return False

result = []

T = int(input())
for i1 in range(T):


    x1, y1, x2, y2 = map(int, input().split())
    distance = (x1-x2)**2 + (y1-y2)**2
    n = int(input())
    count = 0

    for i2 in range(n):
        a, b, c = map(int, input().split())
        if entail(x1, y1, a, b, c) != entail(x2, y2, a, b, c) :
            count = count + 1

    result.append(str(count))
    
print('\n'.join(result))