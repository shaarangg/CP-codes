for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = a[n - 1]
    c = 0
    for i in reversed(range(n)):
        if a[i] > m:
            c += 1
        if a[i] < m:
            m = a[i]
    print(c)
