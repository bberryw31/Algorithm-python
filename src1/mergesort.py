import random

def mergesort(list):
    if len(list) < 2:
        return list
    
    mid = len(list)//2
    lowlist = mergesort(list[:mid])
    highlist = mergesort(list[mid:])

    mergedlist=[]
    a = b = 0
    while len(lowlist) > a and len(highlist) > b:
        if lowlist[a] > highlist [b]:
            mergedlist.append(highlist[b])
            b += 1
        else:
            mergedlist.append(lowlist[a])
            a += 1
    mergedlist += lowlist[a:]
    mergedlist += highlist[b:]
    return mergedlist

def randomlist(N):
    for k in range(int(N)):
        list.append(random.randint(1,9999))

list = []
randomlist(input())
print(mergesort(list))
    

