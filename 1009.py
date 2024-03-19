T = input()

for i in range(int(T)):
    ao, b = map(int, input().split())
    a = ao%10
    x = a
    list = []
    while x not in list:
        list.append(x)
        x = (x * a)%10
    y = b%len(list)
    if 0 in list:
        print(10)
    else:
        if y > 0:
            print(list[y-1])
        else:
            print(list[len(list)-1])

