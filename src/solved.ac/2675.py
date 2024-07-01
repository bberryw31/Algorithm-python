import sys

for j in range(int(sys.stdin.readline())):
    N,txt = sys.stdin.readline().split()
    chrs = []
    chrs.extend(txt)
    result = ""
    for chr in chrs:
        for i in range(int(N)):
            result += chr
    print(result)
