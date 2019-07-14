r=int(input())
c=0
for i in range(1,r+1):
    if r%i==0:
        c=c+1
if c==2:
    print("yes")
else:
    print("no")
