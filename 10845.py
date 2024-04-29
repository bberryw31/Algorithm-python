import sys

N = int(sys.stdin.readline())
queue = []
for i in range(N):
    entry = sys.stdin.readline().strip()
    if "push" in entry:
        queue.append(entry.replace("push ",""))
    elif entry == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif entry == "size":
        print(len(queue))
    elif entry == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif entry == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif entry == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        print("invalid entry")