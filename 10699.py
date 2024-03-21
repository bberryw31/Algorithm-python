import datetime

UTC = datetime.datetime.now()

timediff = datetime.timedelta(hours=9)
KST = UTC + timediff

KSTdate = str(KST).split()
print(KSTdate[0])
