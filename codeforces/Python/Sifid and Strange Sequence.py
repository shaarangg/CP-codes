for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 10 ** 9
    for i in range(n - 1):
        if a[i] > 0:
            break
        if abs(a[i] - a[i + 1]) < m:
            m = abs(a[i] - a[i + 1])
    c = 0
    f = 0
    for i in a:
        if i <= 0:
            c += 1
        elif i > 0 and f == 0 and i <= m:
            c += 1
            f = 1
    print(c)
