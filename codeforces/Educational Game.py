from math import log2

n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n - 1):
    t = int(log2(n - i - 1))
    j = (2 ** t) + i
    s += a[i]
    print(s)
    a[j] += a[i]
