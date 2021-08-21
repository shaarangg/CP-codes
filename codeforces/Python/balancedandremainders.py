t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c=[0,0,0]
    for i in range(n):
        c[a[i]%3]+=1
    j=n//3
    i=0
    count=0
    while(c[0]!=c[1] or c[0]!=c[2]):
        if(c[i]>j):
            c[(i+1)%3]+=c[i]-j
            count+=c[i]-j
            c[i]=j
        i+=1
        i%=3
    res.append(count)
for i in res:
    print(i)