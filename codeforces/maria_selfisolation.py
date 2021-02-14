t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    f=0
    for i in range(n-1,-1,-1):
        if(a[i]<=i+1):
            f=1
            res.append(i+2)
            break
    if(f==0):
        res.append(1)
for i in res:
    print(i)