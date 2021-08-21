t = int(input())
res=[]
for i in range(t):
    n = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    i=0
    while(n[1]>0):
        a.sort()
        b.sort(reverse=True)
        if(a[0]<b[0]):
            a[0]=a[0]+b[0]
            b[0]=a[0]-b[0]
            a[0]=a[0]-b[0]
            n[1]-=1
        else:
            break
    res.append(sum(a))
for i in res:
    print(i)