import random

def selectionsort(list):
    for i in range(len(list)):
        min = list[i]
        for j in range(i, len(list)):
            if list[j] <= min:
                min = list[j]
                minorder = j
        list[i], list[minorder] = list[minorder], list[i]

def randomlist(N):
    for k in range(N):
        list.append(random.randint(1,9999))

list=[]
N = int(input())
randomlist(N)

list2 = [] + list
selectionsort(list)
list2.sort()

print(list)
print(list2)

print(list2==list)

