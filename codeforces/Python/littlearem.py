t = int(input())
res=[]
for i in range(t):
    n,m = map(int,input().split())
    a=[]
    a.append('W'+'B'*(m-1))
    for i in range(n-1):
        a.append('B'*m)
    res.append(a)
for i in res:
    for j in i:
        print(j)