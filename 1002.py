t = input()
result = []
for i in range(int(t)):
    a, b, x, c, d, y = map(int,input().split())
    if a==c and b==d:
        if x==y:
            result.append(-1)
        else:
            result.append(0)
    elif (x+y)**2 > (a-c)**2 + (b-d)**2:
        if (max(x,y) - min(x,y))**2 == (a-c)**2 + (b-d)**2:
            result.append(1)
        elif (max(x,y) - min(x,y))**2 > (a-c)**2 + (b-d)**2:
            result.append(0)
        else:
            result.append(2)
    elif (x+y)**2 == (a-c)**2 + (b-d)**2:
        result.append(1)
    else:
        result.append(0)

for i in range(int(t)):
    print(result[i])