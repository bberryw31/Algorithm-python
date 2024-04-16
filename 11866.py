import sys

N,K = map(int, sys.stdin.readline().split())
l1 = list(range(1,N+1))
l2 = []+l1
out = []
idx = -1
while len(l2)>0:
    idx += K
    while idx > len(l1)-1:
        l1+=l2
    out.append(l1[idx])
    l2.remove(l1[idx])
print("<" + ", ".join(str(x) for x in out) + ">")