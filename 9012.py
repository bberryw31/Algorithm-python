N = int(input())
parenthesis = [("(",")"),("[","]")]
for k in range(N):
    txt = []
    txt.extend(input())
    i = 0
    while i<len(txt)-1 and len(txt)>0:
        if (txt[i],txt[i+1]) in parenthesis:
            del txt[i:i+2]
            i = 0
        else:
            i+=1
    if len(txt)>0:
        print("NO")
    else:
        print("YES")
