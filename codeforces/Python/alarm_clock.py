import math
n = int(input())
res=[]
for i in range(n):
    a,b,c,d=map(int,input().split())
    if(b<a and c<=d):
        res.append(-1)
    else:
        if(b<a):
            total=b
            e=math.ceil((a-b)/(c-d))
            total=total+ e*c
            res.append(total)
        else:
            res.append(b)
for i in res:
    print(i)