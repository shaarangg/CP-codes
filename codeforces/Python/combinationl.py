n = int(input())
a=input()
b=input()
s=0
def frotate(c,d):
    if(c>d):
        return c-d
    else:
        return 10-d+c
def brotate(c,d):
    if(c>d):
        return 10-c+d
    else:
        return d-c
for i in range(n):
        s+=min(brotate(int(a[i]),int(b[i])),frotate(int(a[i]),int(b[i])))
print(s)

