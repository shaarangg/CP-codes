t = int(input())
res=[]
for i in range(t):
    n,k= map(int,input().split())
    s=0
    if(k<=n):
        s= k+n
        if(s%2==0):
            res.append(0)
        else:
            res.append(1)
    else:
        res.append(k-n)
for i in res:
    print(i)