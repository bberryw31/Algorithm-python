def merge(lists,x,K):
    result = 0
    if len(lists) > 1 and len(lists)+1>K:
        for i in range(lists[0],lists[len(lists)-K+1]):
            if i == lists[0]:
                result += 2**i
            elif i not in lists:
                result += 2**i
        return result
    if len(lists) == 1:
        for i in range(lists[0],x):
            if i == lists[0]:
                result += 2**i
            elif i not in lists:
                result += 2**i
        return result
    if len(lists) == 0:
        return K-1

N, K = map(int, input().split())

lists = []
x = 0

while N > 1:
    if N + len(lists) > K and N//2 + len(lists) + 1 > K:
        if N%2 == 0:
            N = N//2
            x += 1
        else:
            N = N//2
            lists.append(x)
            x += 1
    elif N + len(lists) == K:
        print(0)
    else:
        if N%2 == 0:
            N = N//2
            x += 1
        else:
            N = N//2
            lists.append(x)
            x += 1
        add = K - len(lists) - 1
        print(min(merge(lists,x,K),add))
        exit()
print(merge(lists,x,K))








