n, b, p = map(int, input().split())
x, y = 0, n * p
while n > 1:
    x += (n // 2) * b * 2 + n // 2
    if n % 2 == 0:
        n //= 2
    else:
        n //= 2
        n += 1
print("{} {}".format(x, y))
