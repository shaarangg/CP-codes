t = int(input())
res=[]
for i in range(t):
    n,m,x,y=map(int,input().split())
    cost=0
    if(2*x<=y):
        for j in range(n):
            a = input()
            b=a.count('.')
            cost+=b*x
    else:
        for j in range(n):
            a = input()
            cb=0
            for k in a:
                if(k=='*'):
                    cost+=(cb//2)*y + (cb%2)*x
                    cb=0
                else:
                    cb+=1
            cost+=(cb//2)*y + (cb%2)*x
    res.append(cost)
for i in res:
    print(i)