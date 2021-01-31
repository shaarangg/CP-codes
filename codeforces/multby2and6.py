import math
t = int(input())
res=[]
for i in range(t):
    a = int(input())
    c=0
    n=a
    b=[]
    while(a>1):
        if(a%6==0):
            a//=6
            c+=1
        elif(a%3==0):
            a*=2
            c+=1
        else:
            break
    if(a==1):
        res.append(c)
    else:
        res.append(-1)
for i in res:
    print(i)