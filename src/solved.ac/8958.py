import sys
for i in range(int(sys.stdin.readline())):
    ox = sys.stdin.readline()
    streak = 0
    score = 0
    for o in ox:
        if o == "O":
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)
