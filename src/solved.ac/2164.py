import sys

N = int(sys.stdin.readline())
cards = [x for x in range(1,N+1)]
counter = 0
while len(cards)>2:
    counter+=len(cards)
    cards = cards[1::2]
    if counter%2==1:
        cards.append(cards.pop(0))
        counter+=1

if len(cards) == 2:
    if counter%2==1:
        print(cards[0])
    else:
        print(cards[1])
else:
    print(cards[0])
