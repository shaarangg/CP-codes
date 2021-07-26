n, k = map(int, input().split())
a = list(map(int, input().split()))
m = 0
c = 0
for i in range(n):
    c += 1
    if i == n - 1:
        if c > m:
            m = c
        break
    if a[i] == a[i + 1]:
        if c > m:
            m = c
        c = 0
print(m)
