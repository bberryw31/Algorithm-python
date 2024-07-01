import sys
T = int(sys.stdin.readline())
for i in range(T):
    input = sys.stdin.readline().strip()
    chrs = []
    chrs.extend(input)
    print(chrs[0]+chrs[len(chrs)-1])