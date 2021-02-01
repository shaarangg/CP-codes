n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()
min=0
for i in range(m-n+1):
    b=a[i+n-1]-a[i]
    if(i==0):
        min=b
    if(b<min):
        min=b
print(min)