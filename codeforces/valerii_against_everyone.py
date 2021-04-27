t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if(len(a)==len(set(a))):
        res.append("NO")
    else:
        res.append("YES")
for i in res:
    print(i)