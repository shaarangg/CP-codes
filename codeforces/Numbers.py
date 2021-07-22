import math

A = int(input())
s = 0
for i in range(2, A):
    temp = A
    while temp > 0:
        s += temp % i
        temp //= i
print("{}/{}".format(s // math.gcd(s,A-2), (A - 2) // ))
