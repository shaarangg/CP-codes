n,t = map(int,input().split())
if(n==1):
    if(t<10):
        print(t)
    else:
        print(-1)
else:
    a = 10**(n-1)
    if(a%t==0):
        print(a)
    else:
        a = (a//t + 1)*t
        if(len(str(a))==n):
            print(a)
        else:
            print(-1)