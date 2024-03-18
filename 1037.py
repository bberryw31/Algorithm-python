N = int(input())

list = []
list += map(int, input().split())
list.sort()

print(list[0] * list[len(list)-1])
