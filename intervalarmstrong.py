y,z=map(int,input().split())
for r in range(y+1,z):
    a=r%10
    j=r//10
    e=j%10
    s=j//10
    h=a**3+e**3+s**3
    if r==h:
        print(h,end=" ")
    else:
        continue
        
