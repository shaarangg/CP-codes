t = int(input())
res=[]
for i in range(t):
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    m=n
    for j in range(n-d+1):
        b=len(set(a[j:j+d]))
        if(b<m):
            m=b
    res.append(m)
for i in res:
    print(i)