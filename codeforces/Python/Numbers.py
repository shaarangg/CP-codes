from math import gcd

A = int(input())
s = 0
c = 0
for i in range(2, A):
    temp = A
    while temp > 0:
        s += temp % i
        temp //= i
    c += 1
common = gcd(s, c)
s = s // common
c = c // common
print("{}/{}".format(s, c))
