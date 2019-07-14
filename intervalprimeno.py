N,Q=map(int,input().split())
for i in range(N+1,Q):
    for a in range(2,i):
        if i%a==0:
            break;
    else:
        print(i,end=' ')
