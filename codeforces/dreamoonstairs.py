import math
n,m = map(int,input().split())
mins = math.ceil(n/2)
if(mins//m==0 and m<=n):
    print(m)
elif(mins%m==0 and m<=n):
    print(mins)
else:
    mins = (mins//m+1)*m
    if(mins<=n):
        print(mins)
    else:
        print(-1)