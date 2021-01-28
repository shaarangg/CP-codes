t = int(input())
res=[]res=[]
for i in range(t):
    x=0
    a = list(map(int,input().split()))
    if(a[2]%2==0):
        x = x+ a[0]*(a[2]//2) - a[1]*(a[2]//2)
    else:
        x = x + a[0]*(a[2]//2 + 1) - a[1]*(a[2]//2)
    res.append(x)
for i in res:
    print(i)