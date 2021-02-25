n,a = map(int,input().split())
c = list(map(int,input().split()))
a-=1
i=1
count=0
if(c[a]):
    count=1
crim=2
while(a-i>=0 or a+i<n):
    l = a-i
    r = a+i
    if(l<0):
        lef = 1
        crim=1
    else:
        lef = c[l]
    if(r>=n):
        rig = 1
        crim=1
    else:
        rig = c[r]
    if(lef and rig):
        count+=crim
    i+=1
print(count)
