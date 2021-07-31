d = {}


def gridTraveler(m, n, d):
    key = "{},{}".format(m, n)
    if key in d:
        return d[key]
    if key[::-1] in d:
        return d[key[::-1]]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    d[key] = gridTraveler(m - 1, n, d) + gridTraveler(m, n - 1, d)
    return d[key]


m, n = map(int, input().split())
print(gridTraveler(m, n, d))
