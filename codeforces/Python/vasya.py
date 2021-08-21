n,m = map(int, input().split())
s=n
while(n>=m):
    s+=n//m
    n = n//m + n%m
print(s)