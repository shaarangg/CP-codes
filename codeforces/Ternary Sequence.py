for i in range(int(input())):
    x1, y1, z1 = map(int, input().split())
    x2, y2, z2 = map(int, input().split())
    m = min(z1, y2)
    z1 -= m
    s = 2 * m
    m = min(x1 + z1, z2)
    z2 -= m
    if z2 > 0:
        s -= z2 * 2
    print(s)
