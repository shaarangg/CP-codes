t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if(len(set(a))>1):
        b = a.index(max(a))
        if(b==0 and a[0]==a[1]):
            while(a[b]==a[b+1]):
                b+=1
            res.append(b+1)
        elif(b==n-1 and a[b]==a[b-1]):
            while(a[b]==a[b-1]):
                b-=1
            res.append(b+1)
        else:
            res.append(b+1)
    else:
        res.append(-1)
for i in res:
    print(i)