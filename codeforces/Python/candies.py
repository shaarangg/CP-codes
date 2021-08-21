import math
t = int(input())
res=[]
for i in range(t):
    n = int(input())
    k=2
    while(True):
        s = 2**(k)-1
        if(n%s==0):
            res.append(n//s)
            break
        k+=1
for i in res:
    print(i)