import random

def randomlist(length):
    result = []
    for k in range(length):
        result.append(random.randint(1,9999))
    return result

def bubblesort(list):
    for i in range(len(list)):
        for j in range(1, len(list)-i):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]

def compare(list, list2):
    if list == list2:
        return True
    else:
        return False

length = int(input())
list = randomlist(length)
list2=[]
list2.extend(list)

bubblesort(list)
list2.sort()
print(list==list2)

