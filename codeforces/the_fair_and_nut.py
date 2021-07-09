n = int(input())
a = list(map(int, input().split()))
m = 10 ** 9
for i in range(n):
    s = 0
    for j in range(n):
        s += (abs(i - j) + j + i) * 2 * a[j]
    if s < m:
        m = s
print(m)
