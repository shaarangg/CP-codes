n = int(input())
a = list(map(int,input().split()))
c=a[n-1]
for i in reversed(range(n-1)):
    if(a[i+1]<=0):
        break
    elif(a[i]<a[i+1]):
        c+=a[i]
    else:
        c+=a[i+1]-1
        a[i]=a[i+1]-1
print(c)