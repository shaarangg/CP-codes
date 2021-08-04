t = int(input())
res = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    f = 0
    for i in range(n):
        if d.get(a[i], 0) == 0:
            d[a[i]] = [i]
        else:
            d[a[i]] = d[a[i]] + [i]
    for i in d.keys():
        if len(d[i]) >= 3:
            f = 1
            break
        if len(d[i]) == 2 and d[i][1] - d[i][0] >= 2:
            f = 1
            break
    print("YES" if f else "NO")
