t=int(input())
res=[]
for i in range(t):
    n,k = map(int,input().split())
    if(n%2==0):
        n=n+2*k
        res.append(n)
    else:
        s=0
        for i in range(3,n+1):
            if(n%i==0):
                s=i 
                break
        n = n+s+(2*(k-1))
        res.append(n)
for i in res:
    print(i)