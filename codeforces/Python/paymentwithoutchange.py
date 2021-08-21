t = int(input())
res=[]
for i in range(t):
    a,b,n,S = map(int,input().split())
    if(S//n <= a):
        S-=(S//n)*n + b
    else:
        S-=a*n + b
    if(S<=0):
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)