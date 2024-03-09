T=int(input())
for i in range(T):

    n=int(input())

    zerocount={}
    onecount={}

    zerocount[0]=int(1)
    zerocount[1]=int(0)
    onecount[0]=int(0)
    onecount[1]=int(1)


    for x in range(2,n+1):
        zerocount[x] = int(zerocount[x-1])+int(zerocount[x-2])
        onecount[x] = int(onecount[x-1])+int(onecount[x-2])
    
    print(str(zerocount[n])+" "+str(onecount[n]))

