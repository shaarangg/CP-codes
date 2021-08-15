n, q = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
d = {}
res = []
for i in range(n):
    if d.get(a[i], 0) == 0:
        d[a[i]] = i + 1
for i in range(q):
    ans = d[t[i]]
    print(ans)
    d.pop(t[i])
    for keys in d:
        if d[keys] < ans:
            d[keys] += 1
    d[t[i]] = 1
