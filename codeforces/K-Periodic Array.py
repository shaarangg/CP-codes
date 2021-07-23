n, k = map(int, input().split())
a = list(map(int, input().split()))
l = []
j = 0
for i in range(n // k):
    l.append(a[j : j + k])
    j += k
c = 0
for i in range(k):
    d = {}
    for j in range(n // k):
        v = d.get(l[j][i], 0)
        if v == 0:
            d[l[j][i]] = 1
        else:
            d[l[j][i]] = d[l[j][i]] + 1
    if d.get(1, 0) == 0 or d.get(2, 0) == 0:
        continue
    c1 = d.get(1)
    c2 = d.get(2)
    c += c1 if c1 < c2 else c2
print(c)
