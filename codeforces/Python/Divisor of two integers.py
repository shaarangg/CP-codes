n = int(input())
d = list(map(int, input().split()))
if len(d) == 2:
    print("1 1")
else:
    m = max(d)
    i = 1
    while i * i <= m:
        if m % i == 0:
            d.remove(i)
            if i != m // i:
                d.remove(m // i)
        i += 1
    print("{} {}".format(m, max(d)))
