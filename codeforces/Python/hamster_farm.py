N,K = map(int,input().split())
a = list(map(int,input().split()))
p=0
m=10**18
for i in range(K):
    h=N - (N//a[i])*a[i]
    if(h<m):
        m=h
        p=i
print("{} {}".format(p+1,N//a[p]))