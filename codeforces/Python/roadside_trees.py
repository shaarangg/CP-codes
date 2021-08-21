n = int(input())
p=int(input())
t=p+1
for i in range(1,n):
    h=int(input())
    t+=abs(h-p)+2
    p=h
print(t)