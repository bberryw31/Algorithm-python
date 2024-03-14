T = input()

for i in range(int(T)):
    ao, b = map(int, input().split())
    a = ao%10
    x = a
    list = []
    list.append(x)
    for j in range(b-1):
        x = (x * a)%10
        if x not in list:
            list.append(x)
        else:
            break

    y = b%len(list)
    if y > 0:
        print(list[y-1])
    else:
        print(list[len(list)-1])

