r=int(input())
a=r%10
j=r//10
e=j%10
s=j//10
h=a**3+e**3+s**3
if r==h:
    print("yes")
else:
    print("no")
