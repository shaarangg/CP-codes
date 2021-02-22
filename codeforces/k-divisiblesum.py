t = int(input())
res=[]
for i in range(t):
    n,k = map(int,input().split())
    if(n>=k):
        if(n%k==0):
            res.append(1)
        else:
            res.append(2)
    else:
        a = k-n
        if(a%n==0):
            b=a//n
        else:
            b=a//n + 1
        res.append(b+1)
for i in res:
    print(i)