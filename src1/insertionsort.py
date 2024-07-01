import random

def randomlist(N):
    for k in range(int(N)):
        list.append(random.randint(1,9999))

def insertionsort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]

list = []
randomlist(input())
list2 = [] + list
insertionsort(list)
list2.sort()
print(list)
print(list2)
print(list==list2)
