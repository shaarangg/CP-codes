n = int(input())
a = list(map(int,input().split()))
b=[]
b.append("{} {}".format(a[1]-a[0],a[n-1]-a[0]))
for i in range(1,n-1):
    b.append("{} {}".format(min(a[i]-a[i-1],a[i+1]-a[i]),max(a[n-1]-a[i],a[i]-a[0])))
b.append("{} {}".format(a[n-1]-a[n-2],a[n-1]-a[0]))
for i in b:
    print(i)