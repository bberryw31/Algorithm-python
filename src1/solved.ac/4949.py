parenthesis = [("(",")"),("[","]")]
while 1:
    txt = str(input())
    if txt == ".":
        exit()
    else:
        par = []
        for t in txt:
            if t in '()[]':
                par.append(t)
        if len(par)==0:
            print("yes")
        else:
            i = 0
            while i<len(par)-1 and len(par)>0:
                if (par[i],par[i+1]) in parenthesis:
                    del par[i:i+2]
                    i = 0
                else:
                    i+=1
            if len(par)>0:
                print("no")
            else:
                print("yes")