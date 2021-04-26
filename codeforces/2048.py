t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s=0
    f=0
    for j in a:
        if(j>=4096):
            continue
        else:
            s+=j
        if(s>=2048):
            f=1
            res.append("YES")
            break
    if(f==0):
        res.append("NO")
for i in res:
    print(i)