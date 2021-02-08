n=int(input())
a=[]
p=[]
for i in range(n):
    x,y =list(map(int,input().split()))
    a.append(x)
    p.append(y)
min=0
cost=p[0]
for i in range(n):
    if(p[i]>=cost):
        min+=cost*a[i]  
    else:
        cost=p[i]
        min+=cost*a[i]
print(min)