import sys
input = sys.stdin.readline
N,M = map(int,input().split())
poke = {}
poke2 = {}
for i in range(1,N+1):
    ipt = input().strip()
    poke[i] = ipt
    poke2[ipt] = i
for _ in range(M):
    ipt = input().strip()
    try:
        txt = int(ipt)
        print(poke[txt])
    except:
        print(poke2[ipt])