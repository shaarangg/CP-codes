for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = -(10 ** 9)
    s = 0
    for i in a:
        if i > m:
            m = i
        s += i
    s -= m
    ans = (s / (n - 1)) + m
    print("{0:.9f}".format(ans))
