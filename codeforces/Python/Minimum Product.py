t = int(input())
res = []
for i in range(t):
    a, b, x, y, n = map(int, input().split())
    ans = 10 ** 18
    for i in range(2):
        da = min(n, a - x)
        db = min(n - da, b - y)
        ans = min(ans, (a - da) * (b - db))
        a, b = b, a
        x, y = y, x
    res.append(ans)
for i in res:
    print(i)
