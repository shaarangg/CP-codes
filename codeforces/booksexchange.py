t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    nd=""
    for i in range(n):
        c=1
        d=a[i]-1
        while(d!=i):
            d=a[d]-1
            c+=1
        nd+=str(c)+" "
    res.append(nd[:len(nd)-1])
for i in res:
    print(i)
