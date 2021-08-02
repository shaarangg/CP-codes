t = int(input())
res = []
for i in range(t):
    n = int(input())
    a = map(int, input().split())
    if n == 1:
        res.append(0)
    else:
        d = {}
        for i in a:
            if d.get(i, 0) == 0:
                d[i] = 1
            else:
                d[i] += 1
        u = len(d.keys())
        m = 0
        for i in d.keys():
            if d[i] > m:
                m = d[i]
        if u == m:
            res.append(u - 1)
        else:
            res.append(min(u, m))
for i in res:
    print(i)
