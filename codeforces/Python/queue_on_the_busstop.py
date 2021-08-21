n, m = map(int, input().split())
a = list(map(int, input().split()))
i = 0
s = 0
b = 0
while i < n:
    s += a[i]
    if s > m:
        s = 0
        i -= 1
        b += 1
    i += 1
if s != 0:
    b += 1
print(b)
