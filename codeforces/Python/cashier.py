n,L,a = map(int,input().split())
c=0
x=0
for i in range(n):
    t,l = map(int,input().split())
    if(t-x>=a):
        c+=(t-x)//a
    x=t+l
if(L-x>=a):
    c+=(L-x)//a
print(c)