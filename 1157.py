import sys
txt = []
txt.extend((sys.stdin.readline().strip()).lower())
chrs = set(txt)
max = 0
result = []
for chr in chrs:
    if txt.count(chr) > max:
        max = txt.count(chr)
        result = []
        result += chr
    elif txt.count(chr) == max:
        result += chr

if len(result)>1:
    print("?")
elif len(result) == 1:
    print(result[0].upper())
else:
    print("no characters")