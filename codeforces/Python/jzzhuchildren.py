n,m = map(int,input().split())
a = list(map(int,input().split()))
max=0
lh=0
for i in range(n):
    if(a[i]%m==0):
        b = a[i]//m -1
    else:
        b = a[i]//m
    if(b>=max and i>=lh):
        max=b
        lh=i
print(lh+1)