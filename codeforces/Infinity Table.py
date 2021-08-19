from math import ceil

for t in range(int(input())):
    k = int(input())
    n = ceil(k ** (0.5))
    diff = (n ** 2) - k
    r = -1
    c = -1
    if diff < n:
        r = n
        c = diff + 1
    else:
        c = n
        r = (k - ((n ** 2) - ((n - 1) * 2))) + 1
    print("{} {}".format(r, c))
