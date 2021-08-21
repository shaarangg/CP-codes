n, a, b = map(int, input().split())
if n > a * b:
    print(-1)
else:
    c = [[0 for j in range(b)] for i in range(a)]
    p = 1
    i = 0
    j = 0
    while p <= n:
        if i % 2 == 0:
            for j in range(b):
                if p > n:
                    break
                c[i][j] = p
                p += 1
        else:
            for j in reversed(range(b)):
                if p > n:
                    break
                c[i][j] = p
                p += 1
        i += 1
    for i in range(a):
        print(*c[i])
