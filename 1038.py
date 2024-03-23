def dictmaker(dict, prevdict, minnum):
    global count
    tempnums = []
    for a in range(1,10):
        proper_a = 0
        for b in range(1,a): 
            for dics in range(minnum,b+1):
                for j in range(len(prevdict[dics])):
                    temp = str(dics) + str(prevdict[dics][j])
                    tempnums.append(int(temp))
            dict[a] = tempnums
            tempnums = []
            proper_a = 1
        if proper_a == 1 and len(dict[a])>0:
            count += len(dict[a])

def finder(dict, number):
    findcount = 0
    targetcount = number - prevcount
    for first in dict:
        for num in dict[first]:
            findcount += 1
            if targetcount == findcount:
                print(str(first)+str(num))
                exit()
    print("failed")

count, prevcount = 9, 9
dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10 = {}, {}, {}, {}, {}, {}, {}, {}, {}

N = int(input())
if N<10:
    print(N)
else:
    templist = []
    for a2 in range(1,10):
        for b2 in range(a2):
            templist.append(b2)
            count += 1
        dict2[a2] = templist
        templist = []

    if N > count:
        prevcount = count
        dictmaker(dict3,dict2,1)
        if N > count:
            prevcount = count
            dictmaker(dict4,dict3,2)
            if N > count:
                prevcount = count
                dictmaker(dict5,dict4,3)
                if N > count:
                    prevcount = count
                    dictmaker(dict6,dict5,4)
                    if N > count:
                        prevcount = count
                        dictmaker(dict7,dict6,5)
                        if N > count:
                            prevcount = count
                            dictmaker(dict8,dict7,6)
                            if N > count:
                                prevcount = count
                                dictmaker(dict9,dict8,7)
                                if N > count:
                                    prevcount = count
                                    dictmaker(dict10,dict9,8)
                                    if N > count:
                                        print(-1)
                                    else:
                                        finder(dict10,N)
                                else:
                                    finder(dict9,N)
                            else:
                                finder(dict8,N)
                        else:
                            finder(dict7,N)
                    else:
                        finder(dict6,N)
                else:
                    finder(dict5,N)
            else:
                finder(dict4,N)
        else:
            finder(dict3,N)
    else:
        finder(dict2,N)
