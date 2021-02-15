t = int(input())
res=[]
for i in range(t):
    a,b,c = map(int,input().split())
    if(c<=a):
        res.append("{} {}".format(-1,b))
    else:
        if(a*b<=c):
            res.append("{} {}".format(b-1,-1))
        else:
            res.append("{} {}".format(1,b))
for i in res:
    print(i)