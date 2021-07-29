from math import ceil, sqrt

n = int(input())
spf = [i for i in range(n + 1)]
for i in range(2, ceil(sqrt(n))):
    if spf[i] == i:
        for j in range(i * i, n + 1, i):
            if spf[j] == j:
                spf[j] = i
s = n
while n > 1:
    n //= spf[n]
    s += n
print(s)
