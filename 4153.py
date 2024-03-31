import sys

while True:
    input = list(map(int, sys.stdin.readline().split()))
    if input == [0,0,0]:
        exit()
    else:
        input.sort()
        if input[0]**2 + input[1]**2 == input[2]**2:
            print("right")
        else:
            print("wrong")