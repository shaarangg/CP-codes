n,c = map(int,input().split())
x = list(map(int,input().split()))
m=0
for i in range(n-1):
    if(x[i]>=c and x[i]-x[i+1]-c>m):
        m=x[i]-x[i+1]-c
print(m)