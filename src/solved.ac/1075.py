X = int(input())
Y = int(input())

list = []

for i in range(100):
    A = (X//100)*100 + int(i)
    if A%Y == 0:
        list.append(int(i))

list.sort()

if list[0]<10:
    print('0' + str(list[0]))
else:
    print(list[0])