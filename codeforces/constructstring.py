import random
import string
res=[]
t = int(input())
for i in range(t):
    a = list(map(int,input().split()))
    s='abcdefghijklmnopqrstuvwxyz'
    c=0
    r=""
    for i in range(a[0]):
        r=r+s[c]
        c+=1
        if(c==a[2]):
            c=0
    res.append(r)
for i in res:
    print(i)