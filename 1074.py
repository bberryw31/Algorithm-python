count = 0

def splitter(x,y,N):
    global count
    if x<2**(N-1):
        if y<2**(N-1): #1
            if N>0:
                splitter(x,y,N-1)
        else: #3
            count += 2**((N-1)*2)*2
            if N>0:
                splitter(x,y-(2**(N-1)),N-1)
    else:
        if y<2**(N-1): #2
            count += 2**((N-1)*2)
            if N>0:
                splitter(x-(2**(N-1)),y,N-1)
        else: #4
            count += 2**((N-1)*2)*3
            if N>0:
                splitter(x-(2**(N-1)),y-(2**(N-1)),N-1)

A, r, c = map(int, input().split())

splitter(c,r,A)
print(count)