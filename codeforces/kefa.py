n = int(input())
a = list(map(int,input().split()))
max=0
for i in range(n-1):
    l=1
    for j in range(i,n-1):
        if(a[j]<=a[j+1]):
            l+=1
        else:
            break
    if(max<l):
        max=l
print(max)