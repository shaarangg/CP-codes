n = int(input())
d=set()
r=set()
for i in range(n):
    a = list(input())
    for j in range(n):
        if(i==j or j==n-i-1):
            d.add(a[j])
        else:
            r.add(a[j])
if(len(r)==1 and len(d)==1 and d!=r):
    print("YES")
else:
    print("NO")