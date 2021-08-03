from math import log2, floor

n = int(input())
name = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
t = floor(log2((n / 5) + 1))
print(t)
if t == 0:
    print(name[n - 1])
else:
    n1 = 5 * ((2 ** t) - 1)
    n -= n1
    print(n)
    n //= 2 ** t
    print(name[n-1])
