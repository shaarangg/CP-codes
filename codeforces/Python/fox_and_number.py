import math
n = int(input())
x = list(map(int,input().split()))
g=x[0]
for i in range(1,n):
    g=math.gcd(g,x[i])
print(g*n)