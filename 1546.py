import sys

N = int(sys.stdin.readline().strip())
scores = list(map(int, sys.stdin.readline().split()))
scores.sort()
hs = scores[len(scores)-1]
newscores = []
for score in scores:
    newscores.append(score/hs*100)
av = 0
for score in newscores:
    av += score
print(av/N)