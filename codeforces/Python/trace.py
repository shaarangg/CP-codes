import math
n = int(input())
r = list(map(int,input().split()))
r.sort()
a=0
if(n%2==0):
    for i in range(0,n,2):
        a+=r[i+1]**2 - r[i]**2
else:
    for i in range(1,n,2):
        a+=r[i+1]**2 - r[i]**2
    a+=r[0]**2
print("{:0.10f}".format(a*math.pi))