n, k = map(int, input().split())
h = list(map(int, input().split()))
m = sum(h[:k])
s = m
index = 1
for i in range(1, n - k + 1):
    s += h[i + k - 1]
    s -= h[i - 1]
    if s < m:
        m = s
        index = i + 1
print(index)
