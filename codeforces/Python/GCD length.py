def length(a):
    c = 0
    while a > 0:
        a //= 10
        c += 1
    return c


prime = [1, 11, 101, 1013, 10007, 100003, 1000003, 10000019, 100030001]
for t in range(int(input())):
    a, b, c = map(int, input().split())
    gcd = prime[c - 1]
    x = y = gcd
    while True:
        x *= 2
        if length(x) == a:
            break
    while True:
        y *= 3
        if length(y) == b:
            break
    print("{} {}".format(x, y))
