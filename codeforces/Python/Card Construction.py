from math import floor

for i in range(int(input())):
    n = int(input())
    a = 3
    b = 1
    s = 0
    while n > 1:
        c = -2 * n
        d = b ** 2 - (4 * a * c)
        h = floor((-b + d ** (0.5)) / (2 * a))
        n -= (h * (3 * h + 1)) // 2
        # print("{} {} {}".format(d, h, n))
        s += 1
    print(s)
