import sys

N = int(sys.stdin.readline())
stack1, stack2, nums, how = [], [], [], []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
pool = [int(x) for x in range(1,N+1)]
change = True
while change==True:
    change = False
    if len(stack1)>0 and stack1[-1] == nums[0]:
        stack2.append(stack1.pop(-1))
        del nums[0]
        how.append("-")
        change = True
    elif len(pool)>0 and len(stack2)<N:
        stack1.append(pool.pop(0))
        how.append("+")
        change = True
if len(stack2) == N:
    for r in how:
        print(r)
else:
    print("NO")