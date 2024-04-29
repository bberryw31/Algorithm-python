import sys

N = int(sys.stdin.readline())
deque = []
for i in range(N):
    entry = sys.stdin.readline().strip()
    if "push_front" in entry:
        deque.insert(0,entry.replace("push_front ",""))
    elif "push_back" in entry:
        deque.append(entry.replace("push_back ",""))
    elif entry == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif entry == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(-1))
    elif entry == "size":
        print(len(deque))
    elif entry == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif entry == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif entry == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
    else:
        print("invalid entry")