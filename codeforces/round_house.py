n,a,b = map(int,input().split())
k=0
if(b>0):
    if(b%n==0):
        b=n
    else:
        b=b%n
    k=(a+b)%n
    if(k==0):
        k=n
    print(k)
else:
    if(abs(b)%n==0):
        b=-n
    else:
        b=-((abs(b))%n)
    k = (a + n + b)%n
    if(k==0):
        k=n
    print(k)