t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a= list(map(int,input().split()))
    a=list(set(a))
    a.sort()
    if(len(a)>n):
        res.append(n)
    else:
        res.append(len(a))
for i in res:
    print(i)