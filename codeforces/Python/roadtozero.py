t = int(input())
res=[]
for i in range(t):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    mind=0
    if(x>y):
        mind+=(x-y)*a
        x=y
        mind+=min(x*b, x*a*2)
    elif(x==y):
        mind+=min(x*b, x*a*2)
    else:
        mind+=(y-x)*a
        y=x
        mind+=min(y*b, y*a*2)
    res.append(mind)
for i in res:
    print(i)