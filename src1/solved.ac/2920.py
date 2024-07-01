import sys
asc = [1,2,3,4,5,6,7,8]
dsc = [8,7,6,5,4,3,2,1]
input = list(map(int, sys.stdin.readline().split()))

if input == asc:
    print("ascending")
elif input == dsc:
    print("descending")
else:
    print("mixed")