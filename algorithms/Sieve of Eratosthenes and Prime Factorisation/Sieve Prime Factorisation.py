from math import sqrt, ceil

n = int(input())
spf = [i for i in range(n + 1)]
for i in range(2, ceil(sqrt(n))):
    if spf[i] == i:
        for j in range(i * i, n + 1, i):
            if spf[j] == j:
                spf[j] = i
pf = set([])
while n != 1:
    pf.add(spf[n])
    n = n // spf[n]
print(pf)
