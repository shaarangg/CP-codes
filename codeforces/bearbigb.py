a = list(map(int,input().split()))
c=0
while(a[0]<=a[1]):
    c+=1
    a[0]*=3
    a[1]*=2
print(c)