t = int(input())
res=[]
def maxser(a,n):
    m=0
    s=a[0]
    if(s>m):
        m=s
    for i in range(1,n):
        s+=a[i]
        if(s>m):
            m=s
    return m
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    res.append(maxser(a,n)+maxser(b,m))
for i in res:
    print(i)