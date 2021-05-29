n,m = map(int,input().split())
l = 0
for i in range(n):
    a = map(int,input().split())
    t=min(a)
    if(t>l):
        l=t
print(l)