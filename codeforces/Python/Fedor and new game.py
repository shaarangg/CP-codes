def calcxor(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    return c


n, m, k = map(int, input().split())
s = []
for i in range(m + 1):
    a = int(input())
    a = format(a, "b")
    a = "0" * (n - len(a)) + a
    s.append(a)
c = 0
for i in range(m):
    if calcxor(s[i], s[m]) <= k:
        c += 1
print(c)
