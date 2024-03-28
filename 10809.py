import sys
letters = 'abcdefghijklmnopqrstuvwxyz'
input = sys.stdin.readline()
word = []
word.extend(input)
result = ""
for letter in letters:
    if letter in word:
        result += str(word.index(letter)) + " "
    else:
        result += "-1 "
print(result)
