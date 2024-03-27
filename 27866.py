import sys

S = sys.stdin.readline()
i = int(sys.stdin.readline())

word = []
word.extend(S)
print(word[i-1])