t = int(input())
res=[]
for i in range(t):
    l,r,d = map(int,input().split())
    if(d<l and d!=1):
        res.append(d)
    elif(d<l and d==1):
        res.append(1)
    else:
        res.append(((r//d)+1)*d)
for i in res:
    print(i)