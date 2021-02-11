n,x = map(int,input().split())
a = min(n,x)
count=0
for i in range(1, a+1):
    if(x%i==0 and x//i<=n):
        count+=1
print(count)