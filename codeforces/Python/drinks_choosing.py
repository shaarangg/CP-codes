import math
n,k = map(int,input().split())
ns=math.ceil(n/2)
d={}
for i in range(n):
    a = int(input())
    if(a in d):
        d[a]+=1
    else:
        d.update({a:1})
c=0
s=0
for i in d:
    if(d[i]%2!=0):
        s+=1
    c+=d[i]//2
if(ns-c>=s):
    print(n)
else:
    print(c*2 + ns-c)