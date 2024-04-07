import sys

def newfloor(prevfloor):
    floor = [sum(prevfloor[:x+1]) for x in range(len(prevfloor))]
    return floor

for i in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    groundfloor = [room for room in range(1,n+1)]
    prevfloor = groundfloor
    for j in range(1,k):
        prevfloor = newfloor(prevfloor)
    print(sum(prevfloor[:n+1]))