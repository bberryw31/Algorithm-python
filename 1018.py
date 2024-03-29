import sys
import math

M,N = map(int, sys.stdin.readline().split())

board = sys.stdin.read().splitlines()
print(board)
targetWB = []
targetBW = []
lineWB = ""
lineBW = ""
order = 0
for i in range(8):
    if order == 0:
        lineWB += "W"
        lineBW += "B"
        order = 1
    else:
        lineWB += "B"
        lineBW += "W"
        order = 0
order = 0
for j in range(8):
    if order == 0:
        targetWB.append(lineWB)
        targetBW.append(lineBW)
        order = 1
    else:
        targetWB.append(lineBW)
        targetBW.append(lineWB)
        order = 0
print(targetWB)
print(targetBW)


WBdiff = 0
BWdiff = 0
WBdiffmin = math.inf
BWdiffmin = math.inf
for p in range(len(board)-7):#vertical diff between board and target
    for k in range(len(board[0])-7): #horizontal diff
        for l in range(p,p+8):#pick each horizontal line
            strip = board[l][k:k+8]#strip vertical
            for o in range(8):
                if strip[o] != targetWB[l-p][o]:
                    WBdiff += 1
                else:
                    BWdiff += 1
        if WBdiff < WBdiffmin:
            WBdiffmin = WBdiff
        if BWdiff < BWdiffmin:
            BWdiffmin = BWdiff
        WBdiff = 0
        BWdiff = 0

print(min(WBdiffmin,BWdiffmin))
            




    