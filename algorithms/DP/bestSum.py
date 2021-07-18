def calc(n, d):
    if n in d:
        return d[n]
    if n == 0:
        return []
    if n < 0:
        return None
    m = None
    for i in p:
        x = calc(n - i, d)
        if x != None:
            x.append(i)
            if m == None or len(x) < len(m):
                m = x
    d[n] = m
    return m


n, *p = map(int, input().split())
print(calc(n, {}))
