N = int(input())
calls=list(map(int,input().split()))

Yfee = 0
Mfee = 0
for call in calls:
    Yfee += (call//30 + 1)*10
    Mfee += (call//60 + 1)*15

if Yfee<Mfee:
    print("Y",Yfee)
elif Mfee<Yfee:
    print("M",Mfee)
else:
    print("Y M",Yfee)
