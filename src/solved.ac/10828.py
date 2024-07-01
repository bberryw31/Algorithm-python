import sys

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    entry = sys.stdin.readline().strip()
    if "push" in entry:
        stack.append(entry.replace("push ",""))
    elif entry == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif entry == "size":
        print(len(stack))
    elif entry == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif entry == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    else:
        print("invalid entry")