import sys
t = int(input())
res=[]
def check(a,b):
    c=0
    if(b==1):
        b+=1
        c+=1
    while(a!=0):
        a//=b
        c+=1
    return c
for i in range(t):
    a,b = map(int,input().split())
    c=0
    m=sys.maxsize
    for i in range(0,7):
        c=check(a,b+i)+i
        if(c<m):
            m=c
    res.append(m)
for i in res:
    print(i)