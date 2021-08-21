n = int(input())
b = list(map(int,input().split()))
a=[]
max=b[0]
a.append(b[0])
s =str(a[0])
for i in range(1,n):
    c=b[i] + max
    a.append(c)
    if(a[i]>max):
        max=a[i]
    s=s+" {}".format(a[i])
print(s)