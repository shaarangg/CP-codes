import math
n = int(input())
a=[]
b=[]
f=0
for i in range(n):
    a.append(int(input()))
    if(a[i]/2 -(a[i]//2) == 0.5 and f==0):
        b.append(math.ceil(a[i]/2))
        f=1
    elif(a[i]/2 -(a[i]//2) == 0.5 and f==1):
        b.append(math.floor(a[i]/2))
        f=0
    else:
        b.append(round(a[i]/2))
for i in b:
    print(i)