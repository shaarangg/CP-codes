def calc(a, x, d):
    if d.get(a, -1) != -1:
        return d[a]
    else:
        c = 1
        t = a
        while a % x == 0:
            c += 1
            a //= x
        d[t] = c
        return d[t]


for t in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    s = 0
    m = 10 ** 9
    index = 0
    for i in range(n):
        temp = calc(a[i], x, d)
        if temp < m:
            m = temp
            index = i
    for i in range(n):
        if i < index:
            s += a[i] * (m + 1)
        else:
            s += a[i] * m
    print(s)
