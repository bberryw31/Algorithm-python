import sys
T = sys.stdin.readline()
input = sorted(list(set(sys.stdin.read().splitlines())),key=lambda a : len(a))
count = 0
temp = []
result = []
for item in input:
    if len(item)>count:
        result += sorted(temp, key=lambda x : x)
        temp = []
        temp.append(item)
        count = len(item)
    else:
        temp.append(item)
result += sorted(temp, key=lambda x : x)
for item in result:
    print(item)
