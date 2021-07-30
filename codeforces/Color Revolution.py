t = int(input())
res = []
for i in range(t):
    n, k = map(int, input().split())
    if k != 1:
        a = (n * (k - 1)) // ((k ** 4) - 1)
    else:
        a = 1
    l = []
    for i in range(4):
        l.append(a * (k ** i))
    res.append(l)
for i in res:
    print(*i)
