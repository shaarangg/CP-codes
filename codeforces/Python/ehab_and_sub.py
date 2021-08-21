n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
print(a[0])
i=1
while(i<k and i<n):
    if(a[i]-a[i-1]==0):
        k+=1
        i+=1
        continue
    print(a[i]-a[i-1])
    i+=1
if(i<k):
    while(i<k):
        print(0)
        i+=1