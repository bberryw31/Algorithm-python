import sys

N = int(sys.stdin.readline())
ppl = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    ppl.append((int(age),name))

ppl_srt = sorted(ppl, key=lambda x:x[0])

for p in ppl_srt:
    print(str(p[0]) + " " + p[1])