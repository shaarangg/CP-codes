t = int(input())
res=[]
for i in range(t):
    x,y = map(int,input().split())
    if(x-y==1):
        res.append("NO")
    else:
        res.append("YES")
for i in res:
    print(i)