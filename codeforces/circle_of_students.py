t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = a.index(1)
    f=1
    nxt=(s+1)%n
    if(a[nxt]-a[s]==1):
        nxt=(s+1)%n
        while(a[nxt]!=1):
            if(a[nxt]-a[s]==1):
                s=(s+1)%n
            else:
                res.append("NO")
                f=0
                break
            nxt=(s+1)%n
    else:
        nxt=s-1
        if(nxt<0):
            nxt=n-1
        while(a[nxt]!=1):
            if(a[nxt]-a[s]==1):
                s-=1
                if(s<0):
                    s=n-1
            else:
                res.append("NO")
                f=0
                break
            nxt=s-1
            if(nxt<0):
                nxt=n-1
    if(f==1):
        res.append("YES")
for i in res:
    print(i)