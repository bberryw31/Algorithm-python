import sys
def round(x):
    a,b = x//1,x%1
    p = []
    p.extend(str(b))
    if int(p[p.index(".")+1]) >= 5:
        return int(a+1)
    else:
        return int(a)

N = int(sys.stdin.readline())
if N == 0:
    print(0)
else:
    scores = []
    cut = round(N*0.15)
    for i in range(N):
        scores.append(int(sys.stdin.readline()))
    scores.sort()
    print(round(sum(scores[cut:len(scores)-cut])/len(scores[cut:len(scores)-cut])))
