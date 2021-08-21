n,m,a = map(int,input().split())
x,y = max(n,m),min(n,m)
s=0
if(x%a==0):
    s=x//a
else:
    s=(x//a)+1
if(a<y):
    y-=a
    if(y%a==0):
        s+=s*(y//a)
    else:
        if(y//a==0):
            s+=s
        else:
            s+=s*((y//a)+1)
print(s)