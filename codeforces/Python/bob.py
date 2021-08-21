n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
i=0
s=0
while(m>0 and i<n and a[i]<0):
    s+=a[i]
    m-=1
    i+=1
print(abs(s))