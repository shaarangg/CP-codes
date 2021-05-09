t = int(input())
res=[]
for i in range(t):
    n,m = map(int,input().split())
    x=0
    c=0
    mi=101
    for j in range(n):
        a = list(map(int,input().split()))
        for k in range(m):    
            if(a[k]<0):
                c+=1
        
            if(abs(a[k])<mi):
                mi=abs(a[k])

            x+=abs(a[k])

    if(c%2==0):
        res.append(x)
    else:
        res.append(x-(2*mi))
for i in res:
    print(i)