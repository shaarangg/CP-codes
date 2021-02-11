t = int(input())
res=[]
for i in range(t):
    n,m,k = map(int,input().split())
    if(n//k>=m):
        res.append(m)
    else:
        x = [0 for i in range(k-1)]
        i=0
        m-=n//k
        while(m>0):
            x[i]+=1
            i+=1
            i%=k-1
            m-=1
        res.append(n//k - max(x))
for i in res:
    print(i)