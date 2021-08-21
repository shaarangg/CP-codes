from math import log10, ceil

t = int(input())
res = []
for i in range(t):
    n = int(input())
    if n < 10:
        res.append(n)
    elif n == 10:
        res.append(9)
    else:
        p = ceil(log10(n))
        c = 9 * p
        d = n // (10 ** (p - 1))
        e = 9 - d
        f = 0
        for i in range(p):
            f += d * (10 ** i)
        if n < f:
            e += 1
        c -= e
        res.append(c)
for i in res:
    print(i)
