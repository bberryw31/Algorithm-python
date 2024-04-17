import sys

def possible(x,y,z,xhori,xvert,xcube):
    list = [1,2,3,4,5,6,7,8,9]
    for num in [1,2,3,4,5,6,7,8,9]:
        if num in xhori[y]:
            list.remove(num)
    for num in [1,2,3,4,5,6,7,8,9]:
        if num in xvert[x] and num in list:
            list.remove(num)
    for num in [1,2,3,4,5,6,7,8,9]:
        if num in xcube[z] and num in list:
            list.remove(num)
    return(list)

def whatcube(x,y):
    if x<3:
        if y<3:
            return [0, x+y*3]
        elif y<6:
            return [3, x+(y-3)*3]
        else:
            return [6, x+(y-6)*3]
    elif x<6:
        if y<3:
            return [1, x-3+y*3]
        elif y<6:
            return [4, x-3+(y-3)*3]
        else:
            return [7, x-3+(y-6)*3]
    else:
        if y<3:
            return [2, x-6+y*3]
        elif y<6:
            return [5, x-6+(y-3)*3]
        else:
            return [8, x-6+(y-6)*3]

def compile(xhori):
    xsdk = []
    for xhor in xhori:
        result = ""
        for num in xhor:
            result += str(num)
        xsdk.append(result)
    return xsdk

def done(xhori):
    zerocount = 0
    for xhor in xhori:
        if 0 in xhor:
            zerocount += 1
    if zerocount == 0:
        return True
    else:
        return False

def export(xhori):
    for xhor in xhori:
        result = ""
        for num in xhor:
            result += str(num)
        print(result)

def guesser(xsdk,x,y,guess):
    phor0,phor1,phor2,phor3,phor4,phor5,phor6,phor7,phor8 = [],[],[],[],[],[],[],[],[]
    phori = [phor0,phor1,phor2,phor3,phor4,phor5,phor6,phor7,phor8]
    for i in range(9):
        phori[i].extend(xsdk[i])
        phori[i] = [int(x) for x in phori[i]]

    pver0,pver1,pver2,pver3,pver4,pver5,pver6,pver7,pver8 = [],[],[],[],[],[],[],[],[]
    pvert = [pver0,pver1,pver2,pver3,pver4,pver5,pver6,pver7,pver8]
    for i in range(9):
        for j in range(9):
            pvert[i].append(phori[j][i])

    pcub1,pcub2,pcub3,pcub4,pcub5,pcub6,pcub7,pcub8,pcub9 = [],[],[],[],[],[],[],[],[]
    pcube = [pcub1,pcub2,pcub3,pcub4,pcub5,pcub6,pcub7,pcub8,pcub9]
    for i in range(3):
        pcub1.extend(hori[i][0:3])
        pcub2.extend(hori[i][3:6])
        pcub3.extend(hori[i][6:9])
        pcub4.extend(hori[i+3][0:3])
        pcub5.extend(hori[i+3][3:6])
        pcub6.extend(hori[i+3][6:9])
        pcub7.extend(hori[i+6][0:3])
        pcub8.extend(hori[i+6][3:6])
        pcub9.extend(hori[i+6][6:9])

    phori[y][x] = guess
    pvert[x][y] = guess
    pcube[whatcube(x,y)[0]][whatcube(x,y)[1]] = guess

    change = True
    while change == True:
        change = False
        for phor in phori:
            for i in range(9):
                if phor[i] == 0:
                    x = i
                    y = phori.index(phor)
                    z = whatcube(x,y)[0]
                    value = [] + possible(x,y,z,phori,pvert,pcube)
                    if len(value) == 1:
                        phori[y][x] = value[0]
                        pvert[x][y] = value[0]
                        pcube[whatcube(x,y)[0]][whatcube(x,y)[1]] = value[0]
                        change = True
        if change == False:
            if done(phori) == True:
                export(phori)
                exit()
            else:
                for phor in phori:
                    for i in range(9):
                        if phor[i] == 0:
                            x = i
                            y = phori.index(phor)
                            z = whatcube(x,y)[0]
                            value = [] + possible(x,y,z,phori,pvert,pcube)
                            value.sort()
                            if len(value) > 0:
                                guesser(compile(phori),x,y,value[0])
                            else:
                                break

sdk = sys.stdin.read().splitlines()
hor0,hor1,hor2,hor3,hor4,hor5,hor6,hor7,hor8 = [],[],[],[],[],[],[],[],[]
hori = [hor0,hor1,hor2,hor3,hor4,hor5,hor6,hor7,hor8]
for i in range(9):
    hori[i].extend(sdk[i])
    hori[i] = [int(x) for x in hori[i]]

ver0,ver1,ver2,ver3,ver4,ver5,ver6,ver7,ver8 = [],[],[],[],[],[],[],[],[]
vert = [ver0,ver1,ver2,ver3,ver4,ver5,ver6,ver7,ver8]
for i in range(9):
    for j in range(9):
        vert[i].append(hori[j][i])

cub1,cub2,cub3,cub4,cub5,cub6,cub7,cub8,cub9 = [],[],[],[],[],[],[],[],[]
cube = [cub1,cub2,cub3,cub4,cub5,cub6,cub7,cub8,cub9]
for i in range(3):
    cub1.extend(hori[i][0:3])
    cub2.extend(hori[i][3:6])
    cub3.extend(hori[i][6:9])
    cub4.extend(hori[i+3][0:3])
    cub5.extend(hori[i+3][3:6])
    cub6.extend(hori[i+3][6:9])
    cub7.extend(hori[i+6][0:3])
    cub8.extend(hori[i+6][3:6])
    cub9.extend(hori[i+6][6:9])

change = True
while change == True:
    change = False
    for hor in hori:
        for i in range(9):
            if hor[i] == 0:
                x = i
                y = hori.index(hor)
                z = whatcube(x,y)[0]
                value = [] + possible(x,y,z,hori,vert,cube)
                if len(value) == 1:
                    hori[y][x] = value[0]
                    vert[x][y] = value[0]
                    cube[whatcube(x,y)[0]][whatcube(x,y)[1]] = value[0]
                    change = True
    if change == False:
        if done(hori) == True:
            export(hori)
        else:
            for hor in hori:
                for i in range(9):
                    if hor[i] == 0:
                        x = i
                        y = hori.index(hor)
                        z = whatcube(x,y)[0]
                        value = [] + possible(x,y,z,hori,vert,cube)
                        value.sort()
                        for v in value:
                            guesser(compile(hori),x,y,v)