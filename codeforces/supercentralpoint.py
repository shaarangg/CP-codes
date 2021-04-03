n = int(input())
a=[]
s=0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    x=a[i][0]
    y=a[i][1]
    r=0
    l=0
    u=0
    d=0
    for j in range(n):
        if(j==i):
            continue
        x1=a[j][0]
        y1=a[j][1]
        if(x1>x and y1==y):
            r+=1
        elif(x1<x and y1==y):
            l+=1
        elif(x1==x and y1<y):
            d+=1
        elif(x1==x and y1>y):
            u+=1
        else:
            continue
    if(r>0 and l>0 and u>0 and d>0):
        s+=1
print(s)