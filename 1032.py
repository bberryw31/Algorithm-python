a = []
b = []
c = []

def compare(a, b):
    for k in range(len(a)):
        if a[k] == b[k]:
            c[k] = a[k]
        else:
            c[k] = '?'

N = int(input())

if N == 1:
    print(input())

else:
    for j in range(N):
        if len(a) == 0:
            a.extend(input())
        elif len(a) > 0 and len(b) == 0:
            b.extend(input())
            c = [] + a
            compare(a, b)
        else:
            a = []
            a.extend(input())
            compare(a, c)

    result = ''.join(c)
    print(result)
