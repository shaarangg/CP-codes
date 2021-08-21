t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n-1):
        if(a[i]>0):
            a[i+1]+=a[i]
            a[i]=0
    res.append(a[n-1])
for i in res:
    print(i)