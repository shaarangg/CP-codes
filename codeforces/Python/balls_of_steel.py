t = int(input())
res=[]
for i in range(t):
    n,k = map(int,input().split())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    m=0
    for i in range(n):
        c=0
        for j in range(n):
            if(j==i):
                continue
            if(abs(a[i][0]-a[j][0])+abs(a[i][1]-a[j][1])<=k):
                c+=1
        if(m<c):
            m=c
    if(m==n-1):
        res.append(1)
    else:
        res.append(-1)
for i in res:
    print(i)