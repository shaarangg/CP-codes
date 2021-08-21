t = int(input())
res=[]
for i in range(t):
    a = list(map(int,input().split()))
    b=3
    c=0
    for i in range(4):
        if(a[i]%2!=0):
            c+=1
        if(a[i]==0):
            b=i
    if(c==4 or (c==3 and b==3) or c==1 or c==0):
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)