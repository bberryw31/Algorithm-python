import sys
input = sys.stdin.readline

L = int(input())
txt = []
txt.extend(input().strip())
alp = [chr(i) for i in range(ord('a'),ord('z')+1)]
alp.insert(0,0)
result = 0
for i in range(len(txt)):
    result += (alp.index(txt[i])*(31**i))%1234567891
print(result)

