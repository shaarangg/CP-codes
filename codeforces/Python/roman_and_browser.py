n,k = map(int,input().split())
a = list(map(int,input().split()))
m=0
for i in range(k):
    c=0
    p=0
    for j in range(n):
        if(j==k*p+i):
            p+=1
        else:
            c+=a[j]
    if(abs(c)>m):
        m=abs(c)
print(m)