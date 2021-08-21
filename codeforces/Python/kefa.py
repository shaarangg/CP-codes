n = int(input())
a = list(map(int,input().split()))
max=0
l=1
for i in range(n-1):
    if(a[i]>a[i+1]):
        if(max<l):
            max=l
        l=1
    else:
        l+=1
if(max<l):
    max=l   
print(max)