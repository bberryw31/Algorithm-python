import sys

N = int(sys.stdin.readline())
ppl = []
for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    ppl.append((a,b))
rank = []
for p1 in ppl:
    bigger = 1
    for p2 in ppl:
        if p1[0]<p2[0] and p1[1]<p2[1]:
            bigger += 1
    rank.append(bigger)
print(" ".join(str(r) for r in rank))