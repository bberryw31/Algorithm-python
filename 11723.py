import sys
input = sys.stdin.readline

S = [0]*21
for i in range(int(input())):
    ipt = input().strip()
    if "add" in ipt:
        S[int(ipt.replace("add ",""))]=1
    elif "remove" in ipt:
        S[int(ipt.replace("remove ",""))]=0
    elif "check" in ipt:
        print(S[int(ipt.replace("check ",""))])
    elif "toggle" in ipt:
        num = int(ipt.replace("toggle ",""))
        if S[num] == 0:
            S[num] = 1
        else:
            S[num] = 0
    elif "all" in ipt:
        S = [1]*21
    elif "empty" in ipt:
        S = [0]*21
    else:
        print("invalid")