import math
a,b,x,y = map(int,input().split())
g = math.gcd(x,y)
c=0
if(g==1):
    print(min(a//x,b//y))
else:
    x//=g
    y//=g
    print(min(a//x,b//y))