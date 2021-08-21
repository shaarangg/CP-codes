t = int(input())
res=[]
def void_absorption(h,n):
    while(h>20 and n>0):
        h= h//2+10
        n-=1
    n=0
    return (h,n)
def lightning_strike(h,m):
    return (h-(m*10),0)
for i in range(t):
    h,n,m=map(int, input().split())
    while((n>0 or m>0) and h>0):
        h,n=void_absorption(h,n)
        h,m=lightning_strike(h,m)
    if(h<=0):
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)