res=[]
t = int(input())
for i in range(t):
    n  =int(input())
    if(n%2020<=n//2020 and n//2020>0):
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)