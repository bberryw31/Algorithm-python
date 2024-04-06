import sys

N,M = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
max = 0
for i in range(len(cards)-2):
    card1 = cards[i]
    for j in range(i+1,len(cards)-1):
        card2 = cards[j]
        for k in range(j+1,len(cards)):
            card3 = cards[k]
            sum = card1+card2+card3
            if sum <= M and sum > max:
                max = sum
print(max)