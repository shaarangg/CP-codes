t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int,input().split()))
    d=[]
    for j in range(n):
        d.append(b[j]-a[j])
    d.insert(0,0)
    d.insert(n+1,0)
    c=0
    flag=1
    for j in range(n+1):
        if(d[j]<0):
            res.append("NO")
            flag=0
            break
        else:
            if(d[j]!=d[j+1]):
                c+=1
    if(flag==1):
        if(c<=2):
            res.append("YES")
        else:
            res.append("NO")
for i in res:
    print(i)