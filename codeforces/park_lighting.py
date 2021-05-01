t = int(input())
res=[]
for i in range(t):
    m,n=list(map(int,input().split()))
    l = m*(n//2) + ((n%2)*((m//2) + m%2))
    res.append(l)
for i in res:
    print(i)