n,x = map(int,input().split())
s=1
c=0
for i in range(n):
    l,r = map(int,input().split())
    c+= (l-s)%x + r-l+1
    s=r+1
print(c)